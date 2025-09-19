# // cuaieuouac 7


def countVowelSubstrings(word: str) -> int:
    vowels = set("aeiou")
    total = 0

    for i in range(len(word)):
        subset = set()

        for char in word[i:]:
            if char not in vowels:
                break

            subset.add(char)

            total += len(subset) == 5

    return total


# print(countVowelSubstrings("cuaieuouac"))  # 7
# print(countVowelSubstrings("aeiouu"))  # 2
# print(countVowelSubstrings("unicornarihan"))  # 0
# print(countVowelSubstrings("bbaeixoubb"))  # 0


import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7], dtype="f")
# print(arr)
# print(arr.dtype)

# arr = np.array([1.1, 2.1, 3.1])
# print(arr)
# print(arr.dtype)
# new_arr = arr.astype("i")
# print(new_arr)
# print(new_arr.dtype)
# print(np.__version__)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1)
print(arr2)

arr = np.concatenate((arr1, arr2), axis=1)

print("concatenate\n", arr, arr.shape)
for item in arr:
    print(item)

print("DONE")


arr = np.stack((arr1, arr2), axis=1)
print("stack\n", arr, arr.shape)

for item in arr:
    print(item)

print("DONE")
