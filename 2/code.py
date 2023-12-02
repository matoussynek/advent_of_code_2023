import re

class Draw:
    def __init__(self, raw_draw):
        self.r = self.g = self.b = 0
        self.parse_raw_draw(raw_draw)
    
    def parse_raw_draw(self, raw_draw):
        for draw_part in raw_draw.split(','):
            number = int(re.search(r'\d+', draw_part).group())
            if 'red' in draw_part:
                self.r = number
            elif 'green' in draw_part:
                self.g = number
            elif 'blue' in draw_part:
                self.b = number
class Game:
    def __init__(self, raw_game):
        self.draws = {}
        self.parse_raw_game(raw_game)
        
    def parse_game_id(self, game_sub):
        m = re.search(r'\d+', game_sub)
        self.id = int(m.group())
        
    def parse_draws(self, draws_sub):
        for i, draw in enumerate(draws_sub.split(';')):
            self.draws[i] = Draw(draw)
            
    def get_highest_draws(self):
        self.highest_draws = {
            'r': 0,
            'g': 0,
            'b': 0
        }
        for draw in self.draws.values():
            self.highest_draws['r'] = max(draw.r, self.highest_draws['r'])
            self.highest_draws['g'] = max(draw.g, self.highest_draws['g'])
            self.highest_draws['b'] = max(draw.b, self.highest_draws['b'])
        
    def parse_raw_game(self, raw_game):
        parts = line.split(':')
        self.parse_game_id(parts[0])
        self.parse_draws(parts[1])
        self.get_highest_draws()
        
        

class Games:
    def __init__(self, max_red=12, max_green=13, max_blue=14):
        self.games = {}
        self.max_red = max_red
        self.max_green = max_green
        self.max_blue = max_blue
    
    def add_game(self, raw_game):
        game = Game(raw_game)
        self.games[game.id] = game
        print(f'parsed game id: {game.id}')
        
    def is_game_possible(self, game):
        return self.max_red >= game.highest_draws['r'] and self.max_green >= game.highest_draws['g'] and self.max_blue >= game.highest_draws['b']
        
    def sum_possible_games(self):
        s = 0
        for i, game in self.games.items():
            if self.is_game_possible(game):
                s += i
        print(f'Total possible sum: {s}')
        
    def sum_smallest_set(self):
        s = 0
        for i, game in self.games.items():
            s += game.highest_draws['r'] * game.highest_draws['g'] * game.highest_draws['b']
        print(f'Sum of smallest sets is: {s}')

games = Games()
with open("./input.txt", "r") as file:
    for line in file.readlines():
        games.add_game(line)

games.sum_possible_games()
games.sum_smallest_set()