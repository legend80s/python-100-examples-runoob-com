import subprocess
import sys
from dataclasses import dataclass
from typing import NamedTuple, cast

import requests
from bs4 import BeautifulSoup

NO_VSCODE_FLAGS = {"--no-open-vscode", "--nvsc"}


def main():
    index, no_open_in_vscode, dry_run = parse_args()

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
        cmd = f"code {created.readme}"
        if dry_run:
            print(f"$ {cmd}")
        else:
            subprocess.run(cmd)


def check_index(index: str) -> int:
    try:
        flt = float(index)
        if flt.is_integer() and flt > 0:
            pass
        else:
            raise ValueError("必须是大于 0 的整数")

        return int(flt)
    except ValueError:
        print("请输入一个**正整数**")
        sys.exit(1)


class Parsed(NamedTuple):
    example_index: int
    no_open_in_vscode: bool
    dry_run: bool


def parse_args() -> Parsed:
    index = -1

    argv = sys.argv

    if len(argv) > 1:
        index = check_index(argv[1])
    else:
        index = check_index(input("请输入 Example 序号: "))

    no_open_in_vscode = any(arg in NO_VSCODE_FLAGS for arg in argv)
    dry_run = "--dry-run" in argv

    return Parsed(index, no_open_in_vscode=no_open_in_vscode, dry_run=dry_run)


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
        info.demo_result = pre.text.strip()

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
""".strip()

    return readme


def write_readme(readme: str, readme_file_path: str) -> None:
    with open(readme_file_path, "w", encoding="utf-8") as f:
        f.write(readme)


class FilesAndFolders(NamedTuple):
    folder: str
    readme: str
    python: str


def create_files(info: ExampleInfo, dry_run: bool) -> FilesAndFolders:
    index = info.index

    folder = f"example{index}"
    readme = f"{folder}/README.md"
    python = f"{folder}/{index}.py"

    cmd = f"mkdir {folder} && touch {readme} && touch {python}"

    result = FilesAndFolders(folder=folder, readme=readme, python=python)

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


if __name__ == "__main__":
    main()
