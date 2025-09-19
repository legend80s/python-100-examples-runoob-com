import asyncio
import time
from typing import Callable


def setTimeout(func: Callable, delay: float, *args, **kwargs):
    async def wrapper():
        await asyncio.sleep(delay)
        func(*args, **kwargs)

    task = asyncio.create_task(wrapper())

    return task


def clearTimeout(task: asyncio.Task):
    task.cancel()


# 使用示例
async def example_timeout():
    print("开始")
    start = time.perf_counter()
    task = setTimeout(lambda timeout: print(f"{timeout} 秒后执行"), 2, 2)

    # await asyncio.wait_for(task, timeout=1)

    cancel_task = setTimeout(
        lambda: (clearTimeout(task), print(f"{1} 秒后自动取消")), 1
    )

    await asyncio.gather(task, cancel_task, return_exceptions=True)

    # await task
    end = time.perf_counter()
    print(f"{end - start:.2f}s", "后继续执行其他代码")  # 不会阻塞


def setInterval(func, delay, *args, **kwargs) -> asyncio.Task:
    async def wrapper():
        while True:
            await asyncio.sleep(delay)
            func(*args, **kwargs)

    task = asyncio.create_task(wrapper())

    return task


def clearInterval(task: asyncio.Task):
    task.cancel()


# 使用示例
async def example_interval():
    print("定时器开始")
    task = setInterval(lambda: print("每隔1秒执行"), 1)

    task_cancel = asyncio.create_task(asyncio.sleep(3.5))
    task_cancel.add_done_callback(lambda _: clearInterval(task))

    await asyncio.gather(task, task_cancel, return_exceptions=True)

    print("定时器停止")


def main():
    asyncio.run(example_interval())


if __name__ == "__main__":
    main()
