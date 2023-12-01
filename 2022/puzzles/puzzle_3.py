from pathlib import Path
from typing import List
          

def letter_to_value(letter: str) -> int:
     # abc.. = 1-26
     # ABC.. = 27-52
    if letter.islower():
        return ord(letter.upper()) - 64
    else:
        return ord(letter) - 64 + 26


def parse_line(line: str) -> int:
    # abc : def
    # Line split in half
    # Find common character between two halves
    sack_1 = set([i for i in line[:len(line)//2]])
    sack_2 = set([i for i in line[len(line)//2:]])
    common = sack_1.intersection(sack_2).pop()
    return letter_to_value(common)


def parse_three_lines(lines: List[str]) -> int:
    # Find common character on three line groups
    common = None
    for line in lines:
        if common == None:
            common = set(line)
        else:
            common = common.intersection(line)
    return letter_to_value(common.pop())


if __name__ == "__main__":
    input_file = Path("../input/input_3.txt")
    part_1 = 0
    part_2 = 0

    with open(input_file, 'r') as f:
        buffer = []
        for line in f:
            part_1 += parse_line(line)
            buffer.append(line.strip())
            if len(buffer) == 3:
                part_2 += parse_three_lines(buffer)
                buffer = []

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")