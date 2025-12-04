from io import StringIO
from unittest import result


def part_1():
    # part 1
    test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    # input_src = StringIO(test_data)
    input_src = open('d1_input.txt')

    pointer = 50
    zero_count = 0
    for rotation in input_src:
        rotation = rotation.strip()
        direxion, amount = [rotation[index:end] for index, end in zip([0, 1], [1, None])]
        print(direxion, amount)
        if direxion == "L":
            pointer -= int(amount)
        else:
            pointer += int(amount)

        pointer %= 100
        print(pointer)
        if pointer == 0:
            zero_count += 1

    print(f'Password = {zero_count}')

def part_2():
    # part 1
    test_data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    # input_src = StringIO(test_data)
    input_src = open('d1_input.txt')

    pointer = 50
    zero_count = 0
    for rotation in input_src:
        rotation = rotation.strip()
        direxion, amount = [rotation[index:end] for index, end in zip([0, 1], [1, None])]
        amount = int(amount)

        for _ in range(amount):
            if direxion == "L":
                pointer -= 1
            else:
                pointer += 1

            if pointer == 0 or pointer == 100:
                zero_count += 1
                pointer = 0
            elif pointer < 0:
                pointer += 100

    print(f'Password = {zero_count}')


if __name__ == '__main__':
    # part_1()
    part_2()
