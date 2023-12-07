from util import load_input_file
from typing import List
from math import prod


# T = total time for race
# t = total time button is held
# D = total distance
# D = t * (T - t)
# Max distance -> dD/dt = 0 = T - 2t -> t = T/2



def ways_to_win(times: List[int], distances: List[int]):
    ways = []
    for idx, time in enumerate(times):
        t_max = time // 2
        winning_distance = distances[idx]

        better_times = []
        for t in range(t_max, 0, -1):
            d = t * (time - t)
            if d <= winning_distance:
                break
            better_times.append(t)

        for t in range(t_max+1, time):
            d = t * (time - t)
            if d <= winning_distance:
                break
            better_times.append(t)
        ways.append(len(better_times))
    return ways


def part_one(input_data: List[str]):
    times = [int(i) for i in input_data[0].split(' ')[1:] if i]
    distances = [int(i) for i in input_data[1].split(' ')[1:] if i]
    return prod(ways_to_win(times, distances))


def part_two(input_data: List[str]):
    time = int(''.join(input_data[0].split(' ')[1:]))
    distance = int(''.join(input_data[1].split(' ')[1:]))
    return ways_to_win([time], [distance])[0]

if __name__ == "__main__":
    input_data = load_input_file(6)
    print(f'Part one: {part_one(input_data)}')
    print(f'Part two: {part_two(input_data)}')
