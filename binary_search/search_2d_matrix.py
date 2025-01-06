from typing import List


def search(matrix: List[List[int]], target: int) -> List[int]:
    rows, cols = len(matrix), len(matrix[0])

    top, bot = 0, rows - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return -1, -1

    row = (top + bot) // 2
    left, right = 0, cols - 1
    while left <= right:
        mid = (left + right) // 2
        if target > matrix[row][mid]:
            left = mid + 1
        elif target < matrix[row][mid]:
            right = mid - 1
        else:
            return row, mid

    return -1, -1


if __name__ == "__main__":
    print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16))
