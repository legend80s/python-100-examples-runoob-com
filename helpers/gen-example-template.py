import re
import subprocess
import sys
import shutil

from dataclasses import dataclass
from my_timeit import timeit
from typing import NamedTuple, cast

import requests
from bs4 import BeautifulSoup

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

    indices: list[int] = [
        intArg for arg in argv if arg.isdigit() and (intArg := int(arg)) > 0
    ]

    if len(indices) == 0:
        indices = input_indices()

    no_open_in_vscode = any(arg in NO_VSCODE_FLAGS for arg in argv)
    dry_run = "--dry-run" in argv

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


def main():
    parsed = parse_args()

    with timeit(lambda: f"Example #{','.join(map(str, parsed.example_indices))}"):
        init(parsed)


if __name__ == "__main__":
    main()
