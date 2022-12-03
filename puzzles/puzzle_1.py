import heapq
from pathlib import Path


def largest_nsum(input_file: Path, n: int) -> int:
    """ Return sum of n largest sums from data file """
    heap = []
    current_sum = 0

    with open(input_file, 'r') as f:
        for line in f.readlines():
            if line == '\n':
                heapq.heappush(heap, current_sum)
                current_sum = 0
            else:
                current_sum += int(line)
        return sum(heapq.nlargest(n, heap))

    
if __name__ == "__main__":
    input_file = Path("../input/input_1.txt")

    part1 = largest_nsum(input_file, 1)
    part2 = largest_nsum(input_file, 3)

    print("-- Part1 --")
    print(part1)
    print("-- Part2 --")
    print(part2)
