def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(str):
    res, i = [], 0

    while i < len(str):
        j = i

        while str[j] != "#":
            j += 1

        length = int(str[i:j])

        res.append(str[j + 1 : j + 1 + length])

        i = j + 1 + length

    return res


if __name__ == "__main__":
    k = encode(['aaa#', 'bbbxbd', 'cccccc'])

    print(k)

    z = decode(k)

    print(z)


