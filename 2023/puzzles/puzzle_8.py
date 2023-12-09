from util import load_input_file
from typing import Tuple, Dict
from math import lcm
from copy import deepcopy


class Node:
    def __init__(self, name: str, left: str, right:str):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'{self.name}: ({self.left}, {self.right})'

    @staticmethod
    def from_str(line: str):
        name = line.split('=')[0].strip()
        l,r = line.split('=')[1].strip().split(',')
        left, right = l.replace('(', '').strip(), r.replace(')', '').strip()
        return Node(name, left, right)

 
class Path:
    def __init__(self, path_str: str):
        self.path = path_str
        self.index = 0
    
    def __itr__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if len(self.path) == 0:
            raise StopIteration
        char = self.path[self.index]
        self.index = (self.index + 1) % len(self.path)
        return char


def parse_input(input_data: list[str]) -> Tuple[Path, Dict[str, Node]]:
    path = Path(input_data.pop(0))
    input_data.pop(0)
    nodes = [Node.from_str(line) for line in input_data]
    nodes = {node.name: node for node in nodes}
    return path, nodes


def part_one(nodes: dict[str, Node], path: Path) -> int:
    """ Start at AAA find how many steps to end at ZZZ"""
    start_node, end_node = 'AAA', 'ZZZ'
    steps = 0
    current_node = nodes[start_node]

    while current_node.name != end_node:
        current_direction = path.__next__()
        if current_direction == 'L':
            current_node = nodes[current_node.left]
        elif current_direction == 'R':
            current_node = nodes[current_node.right]
        else:
            raise ValueError(f'Invalid direction: {current_direction}')
        steps += 1
    return steps


def path_length(node: Node, nodes: dict[str, Node], path:Path) -> int:
    """ How long it takes to go from node to a node ending in Z"""
    steps = 0
    current_node = node
    while not current_node.name.endswith('Z'):
        current_direction = path.__next__()
        if current_direction == 'L':
            current_node = nodes[current_node.left]
        elif current_direction == 'R':
            current_node = nodes[current_node.right]
        else:
            raise ValueError(f'Invalid direction: {current_direction}')
        steps += 1
    return steps


def part_two(nodes: dict[str, Node], path: Path) -> int:
    starting_nodes = [node for name, node in nodes.items() if name.endswith('A')]
    path_lengths = []
    for node in starting_nodes:
        path_lengths.append(path_length(node, nodes, deepcopy(path)))
    return lcm(*path_lengths)



path, nodes = parse_input(load_input_file(8))
print(f'Part one: {part_one(nodes, path)}')
print(f'Part two: {part_two(nodes, path)}')
