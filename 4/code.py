import re
class Card:
    def __init__(self, hits, points):
        self.copies = 1
        self.hits = hits
        self.points = points

def intersection(l1, l2):
    return [v for v in l1 if v in l2]

cards = {}

def calculate_points():
    pts = 0
    for k,card in cards.items():
        pts += card.points
    print('Total points:', pts)

def calculate_copies():
    copies = 0
    for i, card in cards.items():
        copies += card.copies
        for j in range(1, card.hits + 1):
            cards[i+j].copies += card.copies
    
    print('Total copies:', copies)

with open("./input.txt", "r") as file:
    for line in file.readlines():
        card_id, rest = line.split(':')
        winning_part, current_part = rest.split('|')
        winning = sorted(winning_part.split())
        current = sorted(current_part.split())
        matched = intersection(winning, current)
        card_points = 2**(len(matched)-1) if len(matched) > 0 else 0
        card_id = int(re.search(r'\d+', card_id).group())
        cards[card_id] = Card(len(matched), card_points)

calculate_points()
calculate_copies()