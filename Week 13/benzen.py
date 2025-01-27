def LMSR1(s):
    s = s + s
    n = len(s) // 2
    f = [-1] * n
    k = 0

    for j in range(1, n):
        i = f[j - k - 1]
        while i != -1 and s[k + i + 1] != s[j]:
            if s[j] < s[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if s[k + i + 1] != s[j]:
            if s[j] < s[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k


def LMSR(s):
    n = len(s)
    res = 0
    l = 0
    while l < n:
        res = l
        r = l
        p = l + 1
        while r < n:
            c = s[p] if p < n else s[p - n]
            if s[r] > c:
                break
            if s[r] < c:
                r = l - 1
            r += 1
            p += 1
        l = max(r, l + p - r)
    return res


def detect(chain):
    chain_r = "".join(reversed(chain))
    i = LMSR(chain)
    i_r = LMSR(chain_r)

    n = len(chain)
    chain = chain + chain

    return (i, i_r, chain[i : i + n], chain[i_r : i_r + n])


if __name__ == "__main__":
    chain = "cba"

    print(detect(chain))
