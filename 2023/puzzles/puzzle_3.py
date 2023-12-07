from util import load_input_file
from typing import List, Set, Tuple, Optional


Number = Tuple[int, int, int]
Symbol = Tuple[int, int, str]

def parse_schematic(input_data: List[str], possible_symbols: Set[str]) -> Tuple[Set[Number], Set[Symbol]]:
    """ Parse schematic into a set of part numbers and part symbols"""
    numbers = set()
    symbols = set()
    for line_number, line in enumerate(input_data):
        current_number_start = None
        for column_number, character in enumerate(line):
            if character.isdigit():
                if current_number_start is None:
                    current_number_start = column_number
                if column_number == len(line) - 1:
                    numbers.add((line_number, current_number_start, int(line[current_number_start:])))
            else:
                if current_number_start is not None:
                    numbers.add((line_number, current_number_start, int(line[current_number_start:column_number])))
                current_number_start = None
                if character in possible_symbols:
                    symbols.add((line_number, column_number, character))
                elif character != '.':
                    raise Exception(f'Unexpected character {character}')
    return numbers, symbols

def symbol_exists(symbols: Set[Symbol], line: int, column: int, possible_symbols: Set[str]) -> bool:
    """ Do we have a symbol at the given line and column?"""
    return any([(line, column, symbol) in symbols for symbol in possible_symbols])

def which_number(numbers: Set[Number], line: int, column: int) -> Optional[Number]:
    """ Which number is at the given line and column?"""
    for number in numbers:
        line_number, column_number, value = number
        if line_number == line and column_number <= column < column_number + len(str(value)):
            return number
    return None

def check_for_adjacent_symbols(symbols: Set[Symbol], input_data: List[str], line: int, column: int, possible_symbols: Set[str]) -> bool:
    """ Check if there is a symbol adjacent to the given line and column"""
    found = False
    # Check line above
    if line > 0:
        found = found or symbol_exists(symbols, line - 1, column, possible_symbols)
    # Check line below
    if line < len(input_data) - 1:
        found = found or symbol_exists(symbols, line + 1, column, possible_symbols)
    # Check column left
    if column > 0:
        found = found or symbol_exists(symbols, line, column - 1, possible_symbols)
    # Check column right
    if column < len(input_data[line]) - 1:
        found = found or symbol_exists(symbols, line, column + 1, possible_symbols)
    # Check diagonal up left
    if line > 0 and column > 0:
        found = found or symbol_exists(symbols, line - 1, column - 1, possible_symbols)
    # Check diagonal up right
    if line > 0 and column < len(input_data[line]) - 1:
        found = found or symbol_exists(symbols, line - 1, column + 1, possible_symbols)
    # Check diagonal down left
    if line < len(input_data) - 1 and column > 0:
        found = found or symbol_exists(symbols, line + 1, column - 1, possible_symbols)
    # Check diagonal down right
    if line < len(input_data) - 1 and column < len(input_data[line]) - 1:
        found = found or symbol_exists(symbols, line + 1, column + 1, possible_symbols)
    return found

def check_for_adjacent_numbers(numbers: Set[Number], input_data: List[str], line: int, column: int) -> Set[Number]:
    """ Check if there is a number adjacent to the given line and column"""
    found = set()
    # Check in all directions
    if line > 0:
        found.add(which_number(numbers, line - 1, column))
    if line < len(input_data) - 1:
        found.add(which_number(numbers, line + 1, column))
    if column > 0:
        found.add(which_number(numbers, line, column - 1))
    if column < len(input_data[line]) - 1:
        found.add(which_number(numbers, line, column + 1))
    if line > 0 and column > 0:
        found.add(which_number(numbers, line - 1, column - 1))
    if line > 0 and column < len(input_data[line]) - 1:
        found.add(which_number(numbers, line - 1, column + 1))
    if line < len(input_data) - 1 and column > 0:
        found.add(which_number(numbers, line + 1, column - 1))
    if line < len(input_data) - 1 and column < len(input_data[line]) - 1:
        found.add(which_number(numbers, line + 1, column + 1))

    # Remove None values
    return {num for num in found if num is not None}

def check_number(numbers: Set[Number], symbols: Set[Symbol], input_data: List[str], line: int, column: int, value: int, possible_symbols: Set[str]) -> bool:
    return any([check_for_adjacent_symbols(symbols, input_data, line, column + i, possible_symbols) for i in range(len(str(value)))])

def part_one(numbers: Set[Number], symbols: Set[Symbol], input_data: List[str], possible_symbols: Set[str]) -> int:
    total = 0
    for number in numbers:
        line_number, column_number, value = number
        if check_number(numbers, symbols, input_data, line_number, column_number, value, possible_symbols):
            total += value
    return total

def part_two(numbers: Set[Number], symbols: Set[Symbol], input_data: List[str]) -> int:
    total = 0
    possible_gears = set([symbol for symbol in symbols if symbol[2] == '*'])
    for gear in possible_gears:
        line, column, symbol = gear
        adj_numbers = check_for_adjacent_numbers(numbers, input_data, line, column)
        if len(adj_numbers) == 2:
            first, second = adj_numbers
            total += first[2] * second[2]
    return total

if __name__ == '__main__':
    input_data = load_input_file(3)
    possible_symbols = {'#', '$', '%', '&', '*', '+', '-', '/', '=', '@'}
    numbers, symbols = parse_schematic(input_data, possible_symbols)
    print(f'Part one: {part_one(numbers, symbols, input_data, possible_symbols)}')
    print(f'Part two: {part_two(numbers, symbols, input_data)}')
