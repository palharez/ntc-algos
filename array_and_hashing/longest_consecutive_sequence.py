def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in num_set:
            length = 1

            while (n + length) in num_set:
                length += 1

            longest = max(length, longest)

    return longest


if __name__ == "__main__":
    assert longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == 4
