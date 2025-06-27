## 生成题目

会从 `f'https://www.runoob.com/python/python-exercise-example{index}.html'` 抓取题目并且本地生成文件。

比如生成第 9 题：

```sh
uv run helpers/gen-example-template.py 9
```

- `--no-open-vscode`：默认生成后用 VSCode 打开 README，即执行命令 `code example9/README.md`，如果想禁止该行为，可加上 `--no-open-vscode` 或 `--nvsc`。
- `--dry-run`：若不想实际生成文件，只想看输出，可以加上 `--dry-run`。

## 运行

- 运行 python: `❯ uv run example1/permute.py`
- 运行 js: `❯ bun test example1/permute.test.js`
