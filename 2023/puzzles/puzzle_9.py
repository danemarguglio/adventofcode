from util import load_input_file


def parse_input(input_data: list[str]) -> list[int]:
    return [[int(i) for i in line.split(' ')] for line in input_data]


def extrapolate(data: list[int]) -> int:
    sequence = data
    sequences = [data]

    # Keep iterating until the whole sequence is 0
    quit = all([val == 0 for val in sequence])
    while not quit:
        sequence = [sequence[i+1] - sequence[i] for i in range(0, len(sequence)-1)]
        quit = all([val == 0 for val in sequence])
        sequences.append(sequence)

    diffs = []
    for sequence in sequences:
        if len(sequence) == 1:
            sequence = sequence + [0]
        diff = sequence[-1] - sequence[-2]
        diffs.append(diff)
    return sum(diffs) + sequences[0][-1]


def part_one(data: list[int]) -> int:
    return sum([extrapolate(d) for d in data])


def part_two(data: list[int]) -> int:
    """ Functionally the same exrapolation function with input reversed """
    return sum([extrapolate(d[::-1]) for d in data])


input_data = load_input_file(9)
data = parse_input(input_data)

print(f'Part one: {part_one(data)}')
print(f'Part two: {part_two(data)}')
