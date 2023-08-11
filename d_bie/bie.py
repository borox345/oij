def gcd(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


def bief(a, b, c):
    return int(c / gcd(a, b))


if __name__ == "__main__":
    abc = input().split()
    f = int(abc[0])
    s = int(abc[1])
    t = int(abc[2])
    print(bief(f, s, t))
