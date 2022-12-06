from pathlib import Path
from typing import List
import re


class Stacks:
    def __init__(self, n):
        self.n = n
        self.stacks = [list() for i in range(n)]
    

    def push(self, stack_number, value):
        # Space represents no value in the diagram, so we'll just do this
        if value == ' ':
            return
        self.stacks[stack_number].append(value)
    

    def reverse_all(self):
        # Reverse each on of our stacks in place
        for idx in range(self.n):
            self.stacks[idx].reverse()


    def move(self, quantity, source, destination):
        # Move values from source to destination by popping for source and appending to dest
        for _ in range(quantity):
            self.stacks[destination].append(self.stacks[source].pop())


    def move_bulk(self, quantity, source, destination):
        # Move some number of values from source to destination preserving order
        self.stacks[destination].extend([self.stacks[source].pop() for _ in range(quantity)][::-1])


    def get_result(self) -> str:
        # Pop one off of the top of our stacks for results
        return ''.join([i.pop() for i in self.stacks])



def parse_diagram(lines: List[str], n: int) -> Stacks:
    stacks = Stacks(9)
    #[A] [B] [C] [D]...
    # 1   5   9   13
    # Push all values reversed onto the stacks
    for line in lines:
        for i in range(n):
            stacks.push(i, line[4*i + 1])
    
    # Reverse everything since we read top to bottom
    stacks.reverse_all()
    return stacks



if __name__ == "__main__":
    input_file = Path("../input/input_5.txt")

    with open(input_file, 'r') as f:
        diagram = []
        stacks_1 = None
        stacks_2 = None

        for idx, line in enumerate(f):
            if idx < 8:
                diagram.append(line)
            elif idx == 8:
                # 1 2 3 4 5 6 7 8 9
                # We've finished the diagram, generate our structure
                stacks_1 = parse_diagram(diagram, 9)
                stacks_2 = parse_diagram(diagram, 9)
            elif idx == 9:
                # Empty line after diagram
                continue
            else:
                # Instructions begin
                groups = re.findall(r'move (\d+) from (\d+) to (\d+)', line)
                groups = [int(i) for i in groups[0]]
                quantity, source, destination = groups

                # We have 0 indexing, thus the -1s
                stacks_1.move(quantity, source-1, destination-1)
                stacks_2.move_bulk(quantity, source-1, destination-1)

        print(stacks_1.get_result())
        print(stacks_2.get_result())
