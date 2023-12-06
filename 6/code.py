class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance
        self.calculate_options()
    
    def calculate_options(self):
        self.options = {}
        for i in range (self.time):
            distance = i * (self.time - i)
            if distance > self.distance:
                self.options[i] = distance
    
    def get_options(self):
        return len(self.options.keys())

class Races:
    def __init__(self, lines):
        self.races = []
        self.parse_races(lines)
    
    def parse_races(self, lines):
        time_line = lines[0].split(':')[1].split()
        distance_line = lines[1].split(':')[1].split()

        for i in range(len(time_line)):
            self.races.append(Race(int(time_line[i]), int(distance_line[i])))

    def calculate_options(self):
        tot = 1
        for race in self.races:
            tot *= race.get_options()
        print(f"Total options: {tot}")

races = Races(open('./input.txt').readlines())
races.calculate_options()
races_long = Races([x.replace(' ', '') for x in open('./input.txt').readlines()])
races_long.calculate_options()
