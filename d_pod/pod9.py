def convert(list):
    s = [str(i) for i in list]

    res = int("".join(s))

    return res


def divisibilityBy9(n):
    splited_number = [int(x) for x in str(n)]
    splited_number[0] = 1

    final_number = convert(splited_number)

    while final_number % 9 != 0 and splited_number[0] < 9:
        splited_number[0] += 1
        final_number = convert(splited_number)

    return final_number


if __name__ == "__main__":
    number = int(input())
    print(divisibilityBy9(number))
