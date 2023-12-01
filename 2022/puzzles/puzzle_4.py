from pathlib import Path
from typing import List, Tuple


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


    def overlaps_fully(self, other) -> bool:
        """ Return true if two intervals overlap completely"""
        if self.start >= other.start and self.end <= other.end:
            return True
        elif other.start >= self.start and other.end <= self.end:
            return True
        else:
            return False


    def overlaps(self, other) -> bool:
        """ Return true if two intervals overlap at all """
        if self.start >= other.start and self.start <= other.end:
            return True
        elif self.end >= other.start and self.end <= other.end:
            return True
        elif other.start >= self.start and other.start <= self.end:
            return True
        elif other.end >= self.start and other.end <= self.end:
            return True
        else:
            return False


def line_to_intervals(line: str) -> Tuple[Interval, Interval]:
    # Example, two intervals (1,2), (3,4)
    # 1-2,3-4
    interval_str_1, interval_str_2 = line.split(',')
    to_interval = lambda k : Interval(*[int(i) for i in k.split('-')])
    return(to_interval(interval_str_1), to_interval(interval_str_2))



if __name__ == "__main__":
    input_file = Path("../input/input_4.txt")
    part_1 = 0
    part_2 = 0

    with open(input_file, 'r') as f:
        for line in f:
            interval_1, interval_2 = line_to_intervals(line)
            part_1 += int(interval_1.overlaps_fully(interval_2))
            part_2 += int(interval_1.overlaps(interval_2))

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")