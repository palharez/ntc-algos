from collections import defaultdict

def group_anagrams(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()


if __name__ == "__main__":
    print(group_anagrams(["ate", "tea", "nat", "tan", "atn"]))
