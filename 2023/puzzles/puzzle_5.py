from util import load_input_file
from typing import List, Set


class Range:
    def __init__(self, destination: int, source:int, length:int):
        self.destination = destination
        self.source = source
        self.length = length
    
    def __repr__(self):
        return f'Source: {self.source} -> Dest:{self.destination} Len: ({self.length})'
    
    def contains(self, value: int) -> bool:
        return self.source <= value < self.source + self.length


class Map:
    def __init__(self, name:str , data: List[List[str]]):
        self.name = name
        self.data = data

        # Map catagories
        self.source = name.split('-')[0]
        self.destination = name.split('-')[-1]

        self.ranges = Map._generate_ranges(data)

    @staticmethod
    def _generate_ranges(data: List[str]) -> List[Range]:
        return [Range(destination=row[0], source=row[1], length=row[2]) for row in data]     

    def map_value(self, source_value: int) -> int:
        for r in self.ranges:
            r.source <= source_value < r.source + r.length
            if r.source <= source_value < r.source + r.length:
                return r.destination + (source_value - r.source)
        return source_value

    def reverse_map_value(self, destination_value: int) -> List[int]:
        possible_sources = []
        for r in self.ranges:
            if r.destination <= destination_value < r.destination + r.length:
                source_value = r.source + (destination_value - r.destination)
                possible_sources.append(source_value)
        return possible_sources if possible_sources else [destination_value]



    def __repr__(self):
        return f'{self.name}: {len(self.data)}'


class Maps:
    def __init__(self, maps: List[str]):
        self.maps = maps

    def get(self, source: str, destination: str) -> Map:
        for map in self.maps:
            if not destination:
                if map.source == source:
                    return map
            if not source:
                if map.destination == destination:
                    return map
            if map.source == source and map.destination == destination:
                return map
        return None


def load_maps(input_data: List[str]) -> List[Map]:
    maps = []
    current_map = None
    current_rows = []
    for line in input_data:
        if 'map:' in line:
            if current_map == None:
                current_map = line.split(' ')[0].strip()
                continue
            maps.append(Map(current_map, current_rows))
            current_map = line.split(' ')[0].strip()
            current_rows = []
        elif line.strip() == '':
            continue
        else:
            current_rows.append([int(i) for i in line.strip().split(' ')])
    # Edge case: our last map
    maps.append(Map(current_map, current_rows))
    return maps


def get_destination(maps: List[Map], seed: int) -> int:
    """ Maps a seed to its location"""
    current_source = 'seed'
    end_source = 'location'

    source_value = seed
    while current_source != end_source:
        current_map = maps.get(current_source, None)
        current_source = current_map.destination
        destination_value = current_map.map_value(source_value)
        source_value = destination_value

    return source_value


def part_one(input_data: List[str]) -> int:
    seeds_str = input_data.pop(0)
    seeds = [int(i) for i in seeds_str.split(":")[1].strip().split(" ")]
    maps = Maps(load_maps(input_data))
    destinations = [get_destination(maps, seed) for seed in seeds]
    return min(destinations)


def get_possible_vals(maps, possible_values):
    start = 'location'
    current_map = maps.get(None, start)

    while current_map != maps.get('seed', None):
        temp = []
        for val in possible_values:
            temp.extend(current_map.reverse_map_value(val))
        possible_values = temp
        current_map = maps.get(None, current_map.source)
    return possible_values


def part_two(input_data: List[str]) -> int:
    seeds_str = input_data.pop(0)
    seed_ranges = [int(i) for i in seeds_str.split(":")[1].strip().split(" ")]
    seed_ranges = [Range(None, seed_ranges[idx], seed_ranges[idx] + seed_ranges[idx+1])  for idx in range(0, len(seed_ranges)//2, 2)]
    maps = Maps(load_maps(input_data))

    possible_vals = []
    i = 0
    while True:
        vals = get_possible_vals(maps, [i])
        i += 1
        print(vals)

        


    








input_data = load_input_file(5)
print(f'Part One: {part_one(input_data.copy())}')
print(f'Part Two: {part_two(input_data.copy())}')