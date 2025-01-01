from typing import List


def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    rounds = 0
    while l <= r:
        rounds += 1
        m = l + ((r - l) // 2)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m, rounds
    return -1


if __name__ == "__main__":
    print(binary_search(nums=[i * i for i in range(10_000_000)], target=16))
