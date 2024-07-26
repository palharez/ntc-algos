from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    left_max, right_max = height[l], height[r]
    res = 0

    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            res += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            res += right_max - height[r]

    return res


if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
