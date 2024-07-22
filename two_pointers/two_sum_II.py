def two_sum(nubmers, target):
    l, r = 0, len(nubmers) - 1

    while l < r:
        currSum = nubmers[l] + nubmers[r]

        if currSum > target:
            r -= 1

        elif currSum < target:
            l += 1

        else:
            return [l + 1, r + 1]


if __name__ == "__main__":
    assert two_sum(nubmers=[2, 7, 11, 15], target=9) == [1, 2]
