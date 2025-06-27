import time
from contextlib import contextmanager


@contextmanager
def timeit(label: str):
    start = time.perf_counter()

    try:
        yield
    finally:
        end = time.perf_counter()

        print(f"{label} 耗时: {end - start:2f} 秒")
