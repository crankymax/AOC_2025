from io import StringIO


def part_1():
    # part 1
    test_data = """987654321111111
811111111111119
234234234234278
818181911112111"""
    input_src = StringIO(test_data)
    # input_src = open('input.txt')

    tots_out = 0
    for bank in input_src:
        bank = bank.strip()
        print(bank)
        max_jolt = 0
        for pos_1 in range(0, len(bank)):
            for pos_2 in range(pos_1+1, len(bank)):
                if int("".join([bank[pos_1],bank[pos_2]])) > max_jolt:
                    max_jolt = int("".join([bank[pos_1],bank[pos_2]]))
        print(max_jolt)
        tots_out += max_jolt
    print(tots_out)


def part_2():
    # part 2
    # Updated test data to match the problem description
    test_data = """987654321111111
811111111111119
234234234234278
818181911112111"""
    # input_src = StringIO(test_data)
    input_src = open('input.txt')

    tots_out = 0
    for bank in input_src:
        bank = bank.strip()
        bank_len = len(bank)
        max_bats = 12
        
        # Greedy approach using a Monotonic Stack
        # We want to pick 'max_bats' digits to form the largest number.
        stack = []
        for i, digit in enumerate(bank):
            # We can pop from stack if:
            # 1. Stack is not empty
            # 2. Current digit is larger than the top of the stack (we found a better digit)
            # 3. We have enough remaining digits to fill the stack back to size 12
            #    Remaining digits after current 'i' is (bank_len - 1 - i).
            #    We need len(stack) - 1 + 1 (current digit) + remaining >= max_bats
            remaining = bank_len - 1 - i
            while stack and stack[-1] < digit and len(stack) + remaining >= max_bats:
                stack.pop()
            
            if len(stack) < max_bats:
                stack.append(digit)

        result_num = int("".join(stack))
        print(result_num)
        tots_out += result_num
        
    print(f"Total: {tots_out}")

if __name__ == '__main__':
    # part_1()
    part_2()
