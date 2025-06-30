import json
import os
import pickle
import tempfile
from copy import copy, deepcopy
from typing import Any, TypeVar

array = [1, 2, 3, 4]
# array = [1, 2, [3, 4], {"a": 5}]
# array = [1, 2, [3, 4]]

a1 = array[:]
print("01", a1 == array, a1 is array, a1)  # True False

a2 = array.copy()
print("02", a2 == array, a2 is array, a2)  # True False

a3 = deepcopy(array)
print("03", a3 == array, a3 is array, a3)  # True False


T = TypeVar("T")


def copy1(arr: list[T]) -> list[T]:
    return [item for item in arr]


a4 = copy1(array)
print("04", a4 == array, a4 is array, a4)  # True False


def copy2(arr: list[T]) -> list[T]:
    result: list[T] = []
    for item in arr:
        result.append(item)

    return result


print("05", (a5 := copy2(array)) == array, a5 is array, a5)  # True False


def copy3(arr: list[T]) -> list[T]:
    result: list[T] = []
    result.extend(arr)
    return result


print("06", (a6 := copy3(array)) == array, a6 is array, a6)  # True False


def copy7(arr: list[T]) -> list[T]:
    return list(arr)


print("07", (a7 := copy7(array)) == array, a7 is array, a7)  # True False


def copy8(arr: list[T]) -> list[T]:
    return [*arr]


print("08", (a8 := copy8(array)) == array, a8 is array, a8)  # True False


def copy9(arr: list[T]) -> list[T]:
    return copy(arr)


print("09", (a9 := copy9(array)) == array, a9 is array, a9)  # True False


def copy10(arr: list[T]) -> list[T]:
    def identity(x: Any):
        return x

    return list(map(identity, arr))


print(10, (a10 := copy10(array)) == array, a10 is array, a10)  # True False


def copy11(arr: list[T]) -> list[T]:
    # return arr * 2
    return 1 * arr


print(11, (a11 := copy11(array)) == array, a11 is array, a11)  # True False


def copy12[T1](arr: list[T1]) -> list[T1]:
    # return cast(list[T1], []) + arr
    # empty: list[T1] = []; return empty + arr

    return [] + arr  # type: ignore


# def copy12[T1](arr: list[T1]) -> list[T1]:
#     return cast(list[T1], []) + arr

print(12, (a12 := copy12(array)) == array, a12 is array, a12)  # True False


def copy13(arr: list[T]) -> list[T]:
    # return arr * 2
    return json.loads(json.dumps(arr))


print(13, (a13 := copy13(array)) == array, a13 is array, a13)  # True False


def copy14(arr: list[T]) -> list[T]:
    # return arr * 2
    return pickle.loads(pickle.dumps(arr))


print(14, (a14 := copy14(array)) == array, a14 is array, a14)  # True False


def copy15(arr: list[T]) -> list[T]:
    # 为什么 delete=False 能解决问题
    # 当设置 delete=False 时：

    # Python 不会立即锁定文件用于删除

    # 允许其他操作访问该文件

    # 但需要手动管理文件删除，否则会留下临时文件

    # 而 w+ 模式是更优雅的解决方案，因为它完全避免了重新打开文件的需要。
    with tempfile.NamedTemporaryFile(
        mode="w", prefix="copyfile15-", delete=False
    ) as temp_file:
        # 写入数组到临时文件
        temp_file.write(str(arr))
        temp_file.flush()

        temp_file.close()

        # 重新打开文件读取内容
        with open(temp_file.name, "r") as f:
            content = f.read()

            import ast

            copied = ast.literal_eval(content)

            if not isinstance(copied, list):
                raise ValueError("Not Array. invalid file content maybe corrupted")

        # should delete file manually since `delete=False`
        os.unlink(temp_file.name)

    return copied  # type: ignore


print(15, (a15 := copy15(array)) == array, a15 is array, a15)  # True False


def copy16(arr: list[T]) -> list[T]:
    with tempfile.NamedTemporaryFile(mode="w+", prefix="copyfile-") as temp_file:
        # 写入数组到临时文件
        temp_file.write(str(arr))

        # ! 必须从头读取，否则 content 为空字符串！
        temp_file.seek(0)
        content = temp_file.read()
        # print("content", content)
        import ast

        copied = ast.literal_eval(content)

    return copied


print(16, (a16 := copy16(array)) == array, a16 is array, a16)  # True False


def copy17(arr: list[T]) -> list[T]:
    import ast

    return ast.literal_eval(str(arr))


print(17, (a17 := copy17(array)) == array, a17 is array, a17)  # True False


def copy18(arr: list[T]) -> list[T]:
    with tempfile.NamedTemporaryFile(mode="w+", prefix="copyfile18") as temp_file:
        json.dump(arr, temp_file)

        # 同理必须 seek 0
        # json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
        temp_file.seek(0)

        return json.load(temp_file)


print(18, (a18 := copy18(array)) == array, a18 is array, a18)  # True False


def copy19(arr: list[T]) -> list[T]:
    with tempfile.NamedTemporaryFile(mode="w+b", prefix="copyfile19") as temp_file:
        pickle.dump(arr, temp_file)

        # 同理必须 seek 0
        # EOFError: Ran out of input
        temp_file.seek(0)

        return pickle.load(temp_file)


print(19, (a19 := copy19(array)) == array, a19 is array, a19)  # True False
