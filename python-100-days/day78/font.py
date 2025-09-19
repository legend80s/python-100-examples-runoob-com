from matplotlib.font_manager import FontManager

fonts = {font.name for font in FontManager().ttflist}

for f in sorted(fonts):
    print("  ", f)

print(len(fonts))

# import operator


# arr = [
#     ("cherry", 8.1),
#     ("apple", 2.7),
#     ("dict", 1.7),
#     ("books", 4),
# ]

# print(sorted(arr, key=operator.itemgetter(1)))
