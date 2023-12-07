def load_input_file(puzzle_number) -> list[str]:
    """ Load the input file for the given puzzle number """
    file_name = f'../input/input_{puzzle_number}.txt'
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f'File not found: {file_name}')
        return []