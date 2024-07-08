def count_k_times(nums, k):
    hashmap = {}

    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, frequency in hashmap.items():
        buckets[frequency].append(num)

    resp = []

    for i in range(len(buckets) -1, -1, -1):
        for num in buckets[i]:
            resp.append(num)

            if len(resp) == k:
                return resp

if __name__ == "__main__":
    print(count_k_times([1,1,1,2,2,3], 2))
