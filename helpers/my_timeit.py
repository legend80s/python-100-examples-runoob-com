import time
from contextlib import contextmanager
from typing import Callable, NamedTuple, TypeAlias


class LabelFactoryParams(NamedTuple):
    start_time: float
    end_time: float


FuncWithZeroInputParams: TypeAlias = Callable[[], str]


@contextmanager
def timeit(label: str | FuncWithZeroInputParams | Callable[[LabelFactoryParams], str]):
    """
    label 分三种情况
    1. 传入字符串则自动拼接耗时
    2. 传入 0 参数函数则调用函数并自动拼接耗时
    3. 传入 2 参数函数则给函数传入起始时间，自行计算耗时。

    调用示例:

        with timeit(f'函数 Foo'): # 函数 Foo 耗时 1.23 秒
        with timeit(lambda: f'Example #{index}'): # Example #1 耗时 1.23 秒

        with timeit(
            lambda params: f"Example #{parsed.example_index} 耗时 {params.end_time - params.start_time:.3f}s"
        ): # Example #1 耗时 1.234s
            parsed = parseArgs()
            ...
    """
    start_time = time.perf_counter()

    def make_label(short_label: str) -> str:
        return f"{short_label} 耗时: {end_time - start_time:.2f} 秒"

    def gen_label() -> str:
        if isinstance(label, str):
            return make_label(label)
        else:
            import inspect

            params_count = len(inspect.signature(label).parameters)

            if params_count == 0:
                return make_label(label())  # type: ignore

            return label(LabelFactoryParams(start_time, end_time))  # type: ignore

    try:
        yield
    finally:
        end_time = time.perf_counter()

        full_label = gen_label()

        print(full_label)


if __name__ == "__main__":
    ...
