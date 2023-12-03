import re
class PartNumber:
    def __init__(self, number):
        self.number = number
        self.found = False
        self.coordinates = []
        print('Created umber:', number)

class Symbol:
    def __init__(self,symbol):
        self.symbol = symbol
        self.part_numbers = []

part_numbers = []
part_numbers_dict = {}
symbols = []
symbols_dict = {}

def parse_number(m, y):
    number = PartNumber(int(m.group()))
    start_index = m.start()
    end_index = start_index + len(str(number.number))
    for i in range(start_index, end_index):
        part_numbers_dict[(i,y)] = number
        number.coordinates.append((i,y))
    part_numbers.append(number)

def create_symbol_neighbourhood(symbol, x0, y0):
    for i in range(-1,2):
        for j in range(-1,2):
            coordinates = (x0 + j, y0 + i)
            if coordinates in part_numbers_dict:
                part_number = part_numbers_dict[coordinates]
                if not part_number in symbol.part_numbers:
                    symbol.part_numbers.append(part_number)
                    if not part_number.found:
                        part_number.found = True

def parse_symbols():
    for k,v in symbols_dict.items():
        symbol = Symbol(v)
        create_symbol_neighbourhood(symbol, k[0], k[1])
        symbols.append(symbol)

def sum_part_numbers():
    res = 0
    for part_number in part_numbers:
        if part_number.found:
            res +=part_number.number
    print("Total sum of part numbers:", res)

def sum_gear_ratios():
    res = 0
    for symbol in symbols:
        if symbol.symbol == '*' and len(symbol.part_numbers) == 2:
            res += symbol.part_numbers[0].number * symbol.part_numbers[1].number
    print("Total sum of gear ratios is:", res)

with open("./input.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        for m in re.finditer(r'(\d+)', line):
            parse_number(m, y)
        for i, c in enumerate(line):
            if c == '.' or c.isdigit() or c.isspace():
                continue
            symbols_dict[(i,y)] = c
        


parse_symbols()
sum_part_numbers()
sum_gear_ratios()

