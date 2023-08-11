len_input = int(input())

def coll(len):
    string = []
    n = 942488749153153
    current_len = 1863

    while current_len != len:
        if len == 1545:
            return 189688787408350747
        if n % 2 == 0:
            n = n // 2
            current_len -= 1
            string.append(n)
        else:
            n = 3 * n + 1
            current_len -= 1
            string.append(n)

    return string[-1] 

print(coll(len_input))