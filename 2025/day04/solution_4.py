from io import StringIO

TEST_DATA = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def part_1(input_lines):
    grid = {}
    for r, line in enumerate(input_lines):
        for c, char in enumerate(line):
            grid[(r, c)] = char

    result = 0
    for (r, c), val in grid.items():
        if val == '@':
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    if grid.get((r + dr, c + dc)) == '@':
                        neighbors += 1
            
            if neighbors < 4:
                result += 1

    print(f"Part 1 Result: {result}")


def part_2(input_lines):
    grid = {}
    for r, line in enumerate(input_lines):
        for c, char in enumerate(line):
            grid[(r, c)] = char

    total_removed = 0
    while True:
        to_remove = []
        # Identify all accessible rolls in the current state
        for (r, c), val in grid.items():
            if val == '@':
                neighbors = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        if grid.get((r + dr, c + dc)) == '@':
                            neighbors += 1
                
                if neighbors < 4:
                    to_remove.append((r, c))
        
        if not to_remove:
            break
            
        total_removed += len(to_remove)
        # Remove them all simultaneously
        for r, c in to_remove:
            grid[(r, c)] = '.'
            
    print(f"Part 2 Result: {total_removed}")


if __name__ == '__main__':
    # Set to False to run with real input.txt
    USE_TEST_DATA = True

    if USE_TEST_DATA:
        input_src = StringIO(TEST_DATA)
    else:
        input_src = open('input.txt')

    # Read into a list so it can be used by both parts without exhaustion
    # Also strips newlines and filters empty lines
    line_source = [line.strip() for line in input_src if line.strip()]

    # part_1(line_source)
    part_2(line_source)
