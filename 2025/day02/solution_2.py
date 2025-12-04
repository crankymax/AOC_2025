from io import StringIO
from unittest import result


def part_1():
    # part 1
    test_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    # input_src = StringIO(test_data)
    input_src = open('input.txt')

    products = input_src.readline()
    invalid_checksum = 0
    for product in products.split(','):
        first, second = product.split('-')
        first = int(first)
        second = int(second)
        for id in range(first, second + 1):
            id = str(id)
            # print(len(id), id[0:1])
            if len(id) % 2 != 0:
                continue
            num_split = len(id) // 2
            # print(num_split, id[0:num_split], id[num_split:])
            if id[0:num_split] == id[num_split:]:
                invalid_checksum += int(id)

    print(invalid_checksum)


def part_2():
    # part 2
    test_data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    # input_src = StringIO(test_data)
    input_src = open('input.txt')

    products = input_src.readline()
    invalid_checksum = 0
    for product in products.split(','):
        first, second = product.split('-')
        first = int(first)
        second = int(second)
        for prod_id in range(first, second + 1):
            prod_id = str(prod_id)
            # print(len(prod_id), prod_id)
            for pat_len in range(1,(len(prod_id)//2)+1):
                pat = prod_id[0:pat_len]
                for next_pat in range(pat_len,len(prod_id),pat_len):
                    if pat != prod_id[next_pat:next_pat+pat_len]:
                        break
                else:
                    invalid_checksum += int(prod_id)
                    print(f'Pattern {pat} found in {prod_id}')
                    break

    print(invalid_checksum)


if __name__ == '__main__':
    # part_1()
    part_2()
