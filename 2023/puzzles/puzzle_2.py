from util import load_input_file
from typing import List, Dict, Tuple


def process_line(line: str) -> Tuple[int, List[Dict[str, int]]]:
    """ Process a single line of input to extract game number and cube counts. """
    # Splitting the line to extract game number and cube strings
    game_number = int(line.split(":")[0].split(" ")[1])
    game_strs = line.split(":")[1].strip().split(';')
    games = [] 
    for game in game_strs:
        cube_strs = [i.strip() for i in game.split(",")]
        cube_pairs = [i.split(' ') for i in cube_strs]
        cubes = {i[1]: int(i[0]) for i in cube_pairs}
        games.append(cubes)
        
    return game_number, games

def game_is_possible(game: Dict[str, int], max_cubes: Dict[str, int] = {'red': 12, 'green': 13, 'blue': 14}) -> bool:
    """ Check if the game configuration is possible within the max cube limits. """
    for color in max_cubes:
        if color in game and game[color] > max_cubes[color]:
            return False
    return True

def get_min_cubes(games: List[Dict[str, int]]) -> Dict[str, int]:
    """ Determine the minimum number of cubes required for each color. """
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for game in games:
        for color in game:
            min_cubes[color] = max(min_cubes.get(color, 0), game[color])
    return min_cubes

def part_one(input_data: List[str]) -> int:
    total = 0
    for line in input_data:
        game_number, games = process_line(line)
        if all(game_is_possible(game) for game in games):
            total += game_number
    return total

def part_two(input_data: List[str]) -> int:
    total = 0
    for line in input_data:
        _, games = process_line(line)
        cubes = get_min_cubes(games)
        product = 1
        for color in cubes:
            product *= cubes[color]
        total += product
    return total


if __name__ == '__main__':
    input_data = load_input_file(2)
    print(f'Part one: {part_one(input_data)}')
    print(f'Part two: {part_two(input_data)}')
