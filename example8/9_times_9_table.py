def draw_9_x_9_table() -> None:
    for i in range(1, 9 + 1):
        for j in range(1, i + 1):
            print(f"{i}x{j}={i * j}", end=" ")
        print()


draw_9_x_9_table()
