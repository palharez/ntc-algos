def find(nums, target):
    hashmap = {}

    for i, n in enumerate(nums):
        operation = target - n

        if hashmap.get(operation, -1) > 0:
            return [hashmap.get(operation), i]
        
        hashmap[n] = i
