def booth(s):
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
    return s[k : k + n]


def process_file(input_file, output_file):
    with open(input_file, "r") as file:
        words = file.readlines()

    words = [word.strip() for word in words]
    lmsr_words = [(booth(word), word) for word in words]

    lmsr_words.sort()

    with open(output_file, "w") as file:
        for _, word in lmsr_words:
            file.write(word + "\n")


input_file = "words_109583.txt"
output_file = "booth.txt"
process_file(input_file, output_file)
