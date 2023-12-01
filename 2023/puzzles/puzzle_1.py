import re
from typing import List



DIGITS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def load_input_file(puzzle_number) -> list[str]:
    """ Load the input file for the given puzzle number """
    file_name = f'../input/input_{puzzle_number}.txt'
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f'File not found: {file_name}')
        return []


def get_calibration(line: str) -> int:
    """ Calibration for a line is defined by combining first and last digit into a single number """
    first, last = None, None
    for character in line:
        if character.isdigit():
            if first is None:
                first = int(character)
            last = int(character)
    if last == None:
        raise Exception(f"Could not find any digits in {line}")
    return 10*first + last


def get_calibration_2(line: str) -> int:
    """ Part 2: Same thing but with string representations too """
    find_all = lambda in_string, to_find: [k.start() for k in re.finditer(to_find, in_string)]
    
    ints: List[int] = []
    
    # Find index of all digits
    for index, character in enumerate(line):
        if character.isdigit():
            ints.append((index, int(character)))
    
    # Find index of all words representing digits, slow but who cares
    for digit in DIGITS:
        if digit in line:
            for index in find_all(line, digit):
                ints.append((index, DIGITS[digit]))
                
    # Sort tuples by index, get first and last
    ints.sort(key=lambda x: x[0])
    return 10*ints[0][1] + ints[-1][1]

""" Part 1: Find the sum of all calibrations in the input file """
def part_1(lines: List[str]) -> int:
    return sum([get_calibration(line) for line in lines])


""" Part 2: Same thing but with string numbers too """
def part_2(lines: List[str]) -> int:
    return sum([get_calibration_2(line) for line in lines])


if __name__ == "__main__":
    assert(get_calibration('1any_thing_here_1_2_9') == 19)
    assert(get_calibration('19one') == 19)
    assert(get_calibration('1') == 11)
    assert(get_calibration_2('19one') == 11)
    assert(get_calibration_2('eightwo') == 82)

    lines = load_input_file(1)
    print(f"Part 1: {part_1(lines)}")
    print(f"Part 2: {part_2(lines)}")