from dataclasses import dataclass
import os
import subprocess
import sys
from typing import Final, TypeAlias, TypedDict
import requests
from bs4 import BeautifulSoup


def main():
    index = get_example_index()

    # print(f"{index=}")

    info = fetch_example_info(index)

    # print(info)

    create_files(info)

    readme = gen_readme(info)

    # print(readme)

    write_readme(index, readme)


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


def get_example_index() -> int:
    if len(sys.argv) > 1:
        return check_index(sys.argv[1])
    else:
        return check_index(input("请输入 Example 序号: "))


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


def write_readme(index: int, readme: str) -> None:
    with open(f"./example{index}/README.md", "w", encoding="utf-8") as f:
        f.write(readme)


def create_files(info: ExampleInfo) -> None:
    index = info.index

    folder = f"example{index}"

    cmd = f"mkdir {folder} && touch {folder}/README.md && touch {folder}/{index}.py"
    subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
    main()
