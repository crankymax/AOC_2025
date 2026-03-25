from io import StringIO

TEST_DATA = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def part_1(input_lines):
    fresh_ranges = []
    ids_to_check = []
    
    for line in input_lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            fresh_ranges.append((start, end))
        else:
            ids_to_check.append(int(line))
            
    fresh_count = 0
    for ingredient_id in ids_to_check:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        
        if is_fresh:
            fresh_count += 1
            
    print(f"Part 1 Result: {fresh_count}")


def part_2(input_lines):
    ranges = []
    for line in input_lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
            
    if not ranges:
        print("Part 2 Result: 0")
        return
        
    ranges.sort()
    
    # Merge overlapping ranges
    merged = []
    current_start, current_end = ranges[0]
    
    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]
        
        # Check for overlap or adjacency (e.g. 3-5 and 6-8 can merge to 3-8)
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end
            
    merged.append((current_start, current_end))
    
    # Calculate total length
    total_fresh = 0
    for start, end in merged:
        total_fresh += (end - start + 1)
        
    print(f"Part 2 Result: {total_fresh}")


if __name__ == '__main__':
    # Set to False to run with real input.txt
    USE_TEST_DATA = False

    if USE_TEST_DATA:
        input_src = StringIO(TEST_DATA)
    else:
        input_src = open('input.txt')

    # Read into a list so it can be used by both parts without exhaustion
    # Also strips newlines and filters empty lines
    line_source = [line.strip() for line in input_src if line.strip()]

    # part_1(line_source)
    part_2(line_source)
