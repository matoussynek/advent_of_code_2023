import functools 
from functools import total_ordering

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
cards2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

@total_ordering
class Hand:
    def __init__(self, hand_line, cards):
        self.hand, self.bet = hand_line.split()
        self.cards = cards
        self.calculate_hand()

    def calculate_hand(self):
        card_dict = {}
        for c in self.hand:
            if c in card_dict:
                card_dict[c] += 1
            else: card_dict[c] = 1
        
        sorted_counts = sorted(card_dict.values())[::-1]
        if sorted_counts[0] == 5:
            self.count = 6
        elif sorted_counts[0] == 4:
            self.count = 5
        elif sorted_counts[0] == 3 and sorted_counts[1] == 2:
            self.count = 4
        elif sorted_counts[0] == 3:
            self.count = 3
        elif sorted_counts[0] == 2 and sorted_counts[1] == 2:
            self.count = 2
        elif sorted_counts[0] == 2:
            self.count = 1
        else:
            self.count = 0

    def __lt__(self, other):
        if not self.count == other.count:
            return self.count < other.count
        for i in range(5):
            if not self.hand[i] == other.hand[i]:
                return self.cards.index(self.hand[i]) < self.cards.index(other.hand[i])
        return False
    
    def __eq__(self, other):
        return self.count == other.count and self.hand == other.hand

@total_ordering
class HandJokers(Hand):

    def calculate_hand(self):
        card_dict = {}
        jokers = 0
        for c in self.hand:
            if c == 'J':
                jokers +=1
            elif c in card_dict:
                card_dict[c] += 1
            else: card_dict[c] = 1
        
        if len(card_dict.keys()) == 0:
            self.count = 6
            return
        
        sorted_counts = sorted(card_dict.values())[::-1]
        sorted_counts[0] += jokers
        if sorted_counts[0] == 5:
            self.count = 6
        elif sorted_counts[0] == 4:
            self.count = 5
        elif sorted_counts[0] == 3 and sorted_counts[1] == 2:
            self.count = 4
        elif sorted_counts[0] == 3:
            self.count = 3
        elif sorted_counts[0] == 2 and sorted_counts[1] == 2:
            self.count = 2
        elif sorted_counts[0] == 2:
            self.count = 1
        else:
            self.count = 0
    
hands = []
hands_joker = []
with open('./input.txt', "r") as file:
    for line in file.readlines():
        hands.append(Hand(line, cards))
        hands_joker.append(HandJokers(line, cards2))

tot = 0
for i, hand in enumerate(sorted(hands)):
    tot += (i+1)*int(hand.bet)
print("Star 1:", tot)
    
tot2 = 0
for i, hand in enumerate(sorted(hands_joker)):
    tot2 += (i+1)*int(hand.bet)
print("Star 2:", tot2)