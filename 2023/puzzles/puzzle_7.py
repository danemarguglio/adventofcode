from util import load_input_file
from typing import List
from collections import Counter
from functools import cmp_to_key


class Hand:
    ALL_CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    ALL_CARDS_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    def __init__(self, cards: List[str] = [], bid: str = None) -> None:
        self.cards = cards
        self.hand_value = self.get_hand_value(cards)
        self.card_value = self.get_card_value(cards)

        self.hand_value_2 = self.get_hand_value_2(cards)
        self.card_value_2 = self.get_card_value_2(cards)
        self.bid = int(bid)

    @staticmethod
    def compare(hand1: 'Hand', hand2: 'Hand') -> int:
        if hand1.hand_value < hand2.hand_value:
            return -1
        elif hand1.hand_value == hand2.hand_value:
            for idx in range(len(hand1.card_value)):
                if hand1.card_value[idx] < hand2.card_value[idx]:
                    return -1
                elif hand1.card_value[idx] > hand2.card_value[idx]:
                    return 1
            return 0
        else:
            return 1
        
    @staticmethod
    def compare_2(hand1: 'Hand', hand2: 'Hand') -> int:
        if hand1.hand_value_2 < hand2.hand_value_2:
            return -1
        elif hand1.hand_value_2 == hand2.hand_value_2:
            for idx in range(len(hand1.card_value_2)):
                if hand1.card_value_2[idx] < hand2.card_value_2[idx]:
                    return -1
                elif hand1.card_value_2[idx] > hand2.card_value_2[idx]:
                    return 1
            return 0
        else:
            return 1

    def __repr__(self) -> str:
        return f'Hand: {self.cards} - {self.hand_value} - {self.card_value} - {self.bid}'
    
    def get_card_value(self, cards: List[str]) -> int:
        value_array = []
        for card in cards:
            if card not in self.ALL_CARDS:
                raise ValueError(f'Invalid card: {card}')
            value_array.append(self.ALL_CARDS.index(card))
        return value_array
    
    def get_card_value_2(self, cards: List[str]) -> int:
        value_array = []
        for card in cards:
            if card not in self.ALL_CARDS:
                raise ValueError(f'Invalid card: {card}')
            value_array.append(self.ALL_CARDS_2.index(card))
        return value_array
    
    def get_hand_value(self, in_cards: List[str]) -> int:
        cards = Counter(in_cards)

        hand_value = None 
        # 5 of a kind
        if len(cards) == 1:
            hand_value = 1
        elif len(cards) == 2:
            # 4 of a kind
            if 4 in cards.values():
                hand_value = 2
            # Full house
            else:
                hand_value = 3
        elif len(cards) == 3:
            # 3 of a kind
            if 3 in cards.values():
                hand_value = 4
            # 2 pairs
            else:
                hand_value = 5
        elif len(cards) == 4:
            # 1 pair
            hand_value = 6
        else:
            # High card
            hand_value = 7

        return hand_value
    
    def get_hand_value_2(self, in_cards: List[str]) -> int:
        cards = Counter(in_cards)

        if not 'J' in cards:
            return self.get_hand_value(in_cards)
        if len(cards) != 1:
            jokers = cards.pop('J')
            max_count = max(cards.values())
            most_common_cards = [item for item, count in cards.items() if count == max_count]
            most_common_cards = sorted(most_common_cards, key=lambda x: self.ALL_CARDS_2.index(x))
            most_common_cards = most_common_cards[0]
            cards[most_common_cards] += jokers

        hand_value = None 
        # 5 of a kind
        if len(cards) == 1:
            hand_value = 1
        elif len(cards) == 2:
            # 4 of a kind
            if 4 in cards.values():
                hand_value = 2
            # Full house
            else:
                hand_value = 3
        elif len(cards) == 3:
            # 3 of a kind
            if 3 in cards.values():
                hand_value = 4
            # 2 pairs
            else:
                hand_value = 5
        elif len(cards) == 4:
            # 1 pair
            hand_value = 6
        else:
            # High card
            hand_value = 7

        return hand_value


input_data = load_input_file(7)

all_hands = []
for line in input_data:
    hand, bid = line.split(' ')
    hand = Hand(hand, bid)
    all_hands.append(hand)


def part_one():
    hands = sorted(all_hands, key=cmp_to_key(Hand.compare))
    total = 0
    for idx, hand in enumerate(hands):
        total += (len(hands)-idx) * hand.bid
    return total

def part_two():
    hands = sorted(all_hands, key=cmp_to_key(Hand.compare_2))
    total = 0
    for idx, hand in enumerate(hands):
        total += (len(hands)-idx) * hand.bid
    return total

print(f'Part one: {part_one()}')
print(f'Part two: {part_two()}')