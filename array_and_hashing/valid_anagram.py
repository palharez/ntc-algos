def count_string(string):
    hashmap = {}
    for c in string:
        hashmap[c] = hashmap.get(c, 0) + 1
    return hashmap

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_hashmap = count_string(s)
    t_hashmap = count_string(t)

    for k, v, in s_hashmap.items():
        if t_hashmap.get(k, -1) != v:
            return False
    
    return True

def is_anagram_2(s, t):
    return sorted(s) == sorted(t)

