from pathlib import Path


# A Rock - B Paper - C Scissor
# { Opponent Move : Winning move }
winning_move = {
    'a': 'b',
    'b': 'c',
    'c': 'a'
}

# Score = [ Lose = 0 . Draw = 3 . Win = 6] + Value of move]
move_values = {'a': 1, 'b': 2, 'c': 3}


def evaluate_line_part1(line: str) -> int:
    # First column is my opponent's move
    # Second column is my move, but x,y,z instead of a,b,c
    opponent_move, my_move = line.lower().split()

    # convert x,y,z into a,b,c
    translate_my_move = {
        'x': 'a',
        'y': 'b',
        'z': 'c'
    }
    my_move = translate_my_move[my_move]

    # Draw
    if opponent_move == my_move:
        score = 3
    # Win
    elif winning_move[opponent_move] == my_move:
        score = 6
    # Loss
    else:
        score = 0
    
    return score + move_values[my_move]


def evaluate_line_part2(line: str) -> int:
    # First column is my opponent's move
    # Second column is the result of the round
    # X = Lose
    # Y = Draw
    # Z = Win
    opponent_move, result = line.lower().split()

    # Draw
    if result == 'y':
        my_move = opponent_move
        score = 3
    # Loss
    elif result == 'x':
        my_move = winning_move[opponent_move]
        my_move = winning_move[my_move]
        score = 0
    # Lose
    else:
        my_move = winning_move[opponent_move]
        score = 6
    return score + move_values[my_move]
          

if __name__ == "__main__":
    input_file = Path("../input/input_2.txt")

    with open(input_file, 'r') as f:
        score_1 = 0
        score_2 = 0

        for line in f.readlines():
            if line == '\n':
                break
            score_1 += evaluate_line_part1(line)
            score_2 += evaluate_line_part2(line)

        print(f"Score 1: {score_1}")
        print(f"Score 2: {score_2}")
