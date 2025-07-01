import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import NamedTuple, cast

import requests
from bs4 import BeautifulSoup
from my_timeit import timeit

NO_VSCODE_FLAGS = {"--no-open-vscode", "--nvsc"}


class Parsed(NamedTuple):
    example_indices: list[int]
    no_open_in_vscode: bool
    dry_run: bool


def init(parsed: Parsed) -> None:
    indices, no_open_in_vscode, dry_run = parsed

    for index in indices:
        info = fetch_example_info(index)

        dry_run and print(info)  # type: ignore

        created = create_files(info, dry_run)
        dry_run and print(f"{created=}")  # type: ignore

        readme = gen_readme(info)
        dry_run and print(readme)  # type: ignore

        print(f"write README to {created.readme}") if dry_run else write_readme(
            readme, readme_file_path=created.readme
        )

        if no_open_in_vscode:
            pass
        else:
            open_in_vscode(dry_run, created)


def input_indices() -> list[int]:
    try:
        input_str = input("请输入 Example 序号（多个则以空格隔开）: ")
    except KeyboardInterrupt:
        sys.exit(0)

    try:
        return [check_index(str_index) for str_index in re.split(r"\s+", input_str)]
    except ValueError:
        print("请输入**正整数**，Ctr + C 退出。")

        return input_indices()


def check_index(index: str) -> int:
    flt = float(index)
    if flt.is_integer() and flt > 0:
        pass
    else:
        raise ValueError("必须是大于 0 的整数")

    return int(flt)


def parse_args() -> Parsed:
    argv = sys.argv
    # find all integers parse as index
    dry_run = "--dry-run" in argv

    indices: list[int] = [
        intArg for arg in argv if arg.isdigit() and (intArg := int(arg)) > 0
    ]

    if len(indices) == 0:
        indices = to_list(find_range(argv))
        dry_run and print(f"{indices=}")  # type: ignore

        if len(indices) == 0:
            indices = input_indices()

    no_open_in_vscode = any(arg in NO_VSCODE_FLAGS for arg in argv)

    result = Parsed(indices, no_open_in_vscode=no_open_in_vscode, dry_run=dry_run)

    dry_run and print(result)  # type: ignore

    return result


@dataclass
class ExampleInfo:
    index: int
    url: str
    title: str = ""
    hint: str = ""
    demo_result: str = ""


@dataclass(frozen=True)
class Selector:
    title: str
    # hint: str
    demo_result: str


def fetch_example_info(index: int) -> ExampleInfo:
    selector = Selector(title="#content p:has(strong)", demo_result="#content pre")
    url = f"https://www.runoob.com/python/python-exercise-example{index}.html"

    html = requests.get(url).text

    # print(f"{html=}")

    soup = BeautifulSoup(html, "html.parser")
    info = ExampleInfo(index=index, url=url)
    pTags = soup.css.select(selector.title)  # type: ignore

    if not pTags or len(pTags) != 2:
        return info

    p1, p2 = pTags

    info.title = p1.text.strip()
    info.hint = p2.text.strip()

    if pre := soup.css.select(selector.demo_result)[0]:  # type: ignore
        info.demo_result = pre.text.rstrip()

    return info


def gen_readme(info: ExampleInfo) -> str:
    index = info.index
    title = info.title
    hint = info.hint
    demo_result = info.demo_result
    url = info.url

    readme = f"""
# Python Example #{index}

> {title}

## Demo Result

```python
{demo_result}
```

## Hints

{hint}

## References

- <{url}>
""".lstrip()

    return readme


def write_readme(readme: str, readme_file_path: str) -> None:
    with open(readme_file_path, "w", encoding="utf-8") as f:
        f.write(readme)


class CreatedFilesAndFolders(NamedTuple):
    folder: str
    readme: str
    python: str


def create_files(info: ExampleInfo, dry_run: bool) -> CreatedFilesAndFolders:
    index = info.index

    folder = f"example{index}"
    readme = f"{folder}/README.md"
    python = f"{folder}/{index}.py"

    cmd = f"mkdir {folder} && touch {readme} && touch {python}"

    result = CreatedFilesAndFolders(folder=folder, readme=readme, python=python)

    if dry_run:
        print(f"$ {cmd}")
        return result

    try:
        subprocess.run(
            cmd,
            # 运行多条命令
            shell=True,
            # 命令失败 raise
            check=True,
            # 报错的时候能通过 stderr 输出自己想要的内容
            capture_output=True,
            # 输出为解码后文本而非编码，否则自己解码各平台不一样（Linux utf-8，Windows gbk）会多很多代码
            text=True,
        )
    except subprocess.CalledProcessError as err:
        print(cast(str, err.stderr).strip())
        sys.exit(err.returncode)

    return result


def open_in_vscode(dry_run: bool, files: CreatedFilesAndFolders) -> None:
    vscode_cmd = shutil.which("code") or shutil.which("code.cmd")

    if not vscode_cmd:
        print("VS Code 未安装或未添加到 PATH")
        return

    cmd = f"{vscode_cmd} {files.readme}"

    if dry_run:
        print(f"$ {cmd}")
    else:
        subprocess.run(cmd)


class Range(NamedTuple):
    start_inclusive: int
    stop_inclusive: int


def find_range(args: list[str]) -> None | Range:
    matches = (
        Range(int(result["start"]), int(result["stop"]))
        for arg in args
        if (result := re.match(r"(?P<start>\d+)\-(?P<stop>\d+)", arg))
    )

    # 只需要第一项即可，性能相差不大，因为即使有多个也只会匹配到第一个就结束
    return next(matches, None)

    # if + early-return
    # for arg in args:
    #     if result := re.match(r"(?P<start>\d+)\-(?P<stop>\d+)", arg):
    #         return Range(
    #             start_inclusive=int(result["start"]),
    #             stop_inclusive=int(result["stop"]),
    #         )


def to_list(rng: None | Range) -> list[int]:
    return list(range(rng.start_inclusive, rng.stop_inclusive + 1)) if rng else []


def main():
    parsed = parse_args()

    with timeit(
        lambda: f"Example #{' '.join(map(lambda index: f'{index}✅', parsed.example_indices))}"
    ):
        init(parsed)


if __name__ == "__main__":
    main()
    # arg = "15-20"
    # result = re.match(r"(?P<start>\d+)\-(?P<stop>\d+)", arg)
    # if result:
    # print(result.groupdict())
    #     print(result.groups())
    #     print(result.group())
    # args = ["helpers/gen-example-template.py", "15-20", "--dry-run"]
