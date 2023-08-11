# Validate characters and validate_count letters in list
def validate_count(letter):
    valid_characters = []
    for ch in letters:
        if ch in 'OIJE':
            valid_characters.append(ch)

    number = 0
    for x in valid_characters:
        if letter is x:
            number += 1

    return number


def pre():
    result = ['N', 'N', 'N']

    # OIJ
    if validate_count('O') >= 1 and validate_count('I') >= 1 and validate_count('J') >= 1:
        result[0] = 'T'

    # EJIO
    if validate_count('O') >= 1 and validate_count('J') >= 1 and validate_count('I') >= 1 and validate_count('E') >= 1:
        result[1] = 'T'

    # IOI
    if validate_count('O') >= 1 and validate_count('I') >= 2:
        result[2] = 'T'

    print("".join(result))

if __name__ == "__main__":
    letters = list(input())

    pre()
