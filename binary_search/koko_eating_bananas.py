import math
from typing import List


def eating(piles: List[int], hours: int) -> int:
    left, right = 1, max(piles)
    res = right

    while left < right:
        k = (left + right) // 2
        consumed_hours = 0
        for p in piles:
            consumed_hours += math.ceil(p / k)
        if consumed_hours <= hours:
            res = min(res, k)
            right = k - 1
        else:
            left = k + 1

    return res


if __name__ == "__main__":
    print(eating(piles=[3, 6, 7, 1], hours=8))
