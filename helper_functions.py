import numpy as np

board = [0, 0, 4, 5, 1, 9, 0, 0, 0, 6, 1, 0, 0, 7, 0, 0, 5, 9, 0, 0, 0, 6, 3, 0, 0, 0, 0, 5,
         4, 0, 3, 0, 0, 0, 0, 2, 3, 0, 6, 0, 0, 0, 0, 0, 0, 1, 0, 0, 4, 0, 0, 0, 6, 7, 0, 0, 2, 0,
         0, 0, 4, 0, 5, 8, 0, 0, 0, 4, 0, 0, 2, 0, 4, 0, 0, 1, 0, 0, 7, 0, 6]

grid = np.asarray(board).reshape(9, 9)


def possible(bo, y, x, n):
    for i in range(0, 9):
        if bo[y][i] == n:
            return False
    for i in range(0, 9):
        if bo[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if bo[y0 + i][x0 + j] == n:
                return False
    return True


def solve(bo):
    for y in range(9):  # row
        for x in range(9):  # column
            if bo[y][x] == 0:
                for n in range(1, 10):
                    if possible(bo, y, x, n):
                        bo[y][x] = n
                        solve(bo)
                        bo[y][x] = 0
                return
    return bo

solved = solve(grid)
print(solved)
