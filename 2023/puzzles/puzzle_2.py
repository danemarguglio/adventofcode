from util import load_input_file


# e.g. Game 1: 4 red, 8 green; 8 green, 6 red; 13 red, 8 green; 2 blue, 4 red, 4 green
def process_line(line: str):
    game_number = int(line.split(":")[0].split(" ")[1])
    game_strs = line.split(":")[1].strip().split(';')
    games = [] # [{'red': 2, 'blue': 11, 'green': 2}, ... ]
    for game in game_strs:
        cube_strs = [i.strip() for i in game.split(",")]
        cube_pairs = [i.split(' ') for i in cube_strs]
        cubes = {i[1]:int(i[0]) for i in cube_pairs}
        games.append(cubes)
    return game_number, games
    
#  only 12 red cubes, 13 green cubes, and 14 blue cubes   
def game_is_possible(game, max_cubes = {'red': 12, 'green': 13, 'blue': 14 }):
    for color in max_cubes:
        if color not in game:
            continue
        if game[color] > max_cubes[color]:
            return False
    return True

# Get min cubes for a game
def get_min_cubes(games):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for game in games:
        for color in game:
            if color not in min_cubes:
                min_cubes[color] = game[color]
            else:
                min_cubes[color] = max(min_cubes[color], game[color])
    return min_cubes
    

input_data = load_input_file(2)

def part_one(input_data: list[str] = input_data) -> int:
    total = 0
    for line in input_data:
        game_number, games = process_line(line)
        impossible = False
        
        for game in games:
            if not game_is_possible(game):
                impossible = True
                break
        
        if not impossible:
            total += game_number
    return total


def part_two(input_data: list[str] = input_data) -> int:
    total = 0
    for line in input_data:
        game_number, games = process_line(line)
        cubes = get_min_cubes(games)
        product = 1
        for color in cubes:
            product *= cubes[color]
        total += product
    return total
    


print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')