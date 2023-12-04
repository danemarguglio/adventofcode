from util import load_input_file
from typing import List, Set, Tuple, Optional


class Card:
    """ Simple class to represent a card """
    def __init__(self, card_number: int, winning_numbers: List[int], our_numbers: List[int]):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.our_numbers = our_numbers
    
    def __repr__(self):
        return f'Card {self.card_number}: {self.winning_numbers} | {self.our_numbers}'
    
    def matches(self) -> int:
        return sum([1 for number in self.winning_numbers if number in self.our_numbers])
    
    def value(self) -> int:
        """ Calculate the value of the card """
        number_of_matches = self.matches()
        if number_of_matches == 0:
            return 0
        elif number_of_matches == 1:
            return 1
        else:
            return 2 ** (number_of_matches - 1)
    
    
def load_cards(input_data: List[str]) -> List[Card]:
    """ Load cards from input data """
    cards: Card = []
    for line in input_data:
        # Card #: Winning numbers | Our numbers
        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        card_number = int(line.split(':')[0].split(' ')[-1])
        winning_numbers_str, our_numbers_str  = line.split(':')[1].split('|')
        
        def parse_numbers(numbers_str: str) -> List[int]:
            return [int(i) for i in numbers_str.split(' ') if i != '']
        
        winning_numbers = parse_numbers(winning_numbers_str)
        our_numbers = parse_numbers(our_numbers_str)
        cards.append(Card(card_number, winning_numbers, our_numbers))
    return cards


def get_total_value(cards: List[Card]) -> int:
    """ Calculate the total value of all cards """
    return sum([card.value() for card in cards])


def part_one(input_data: List[str]) -> int:
    cards = load_cards(input_data)
    return get_total_value(cards)


def part_two(input_data: List[str]) -> int:
    cards = load_cards(input_data)
    labeled_cards = {card.card_number: card for card in cards}
    card_counts = {card_number: 1 for card_number in labeled_cards}

    for card_number in labeled_cards:
        n_cards = card_counts[card_number]
        n_matches = labeled_cards[card_number].matches()
        
        for i in range(card_number + 1, card_number + 1 +n_matches):
            card_counts[i] += n_cards
        
    return sum(card_counts.values())


example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')
assert part_one(example) == 13
assert part_two(example) == 30


input_data = load_input_file(4)
print(f"Part one: {part_one(input_data)}")
print(f"Part two: {part_two(input_data)}")