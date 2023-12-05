import sys
class Rule:
    def __init__(self, rule_line):
        #print(f'Creating rule: {rule_line}')
        rule_splits = rule_line.split()
        self.dest_start = int(rule_splits[0])
        self.src_start = int(rule_splits[1])
        self.range = int(rule_splits[2])
    
    def fits(self, n):
        return n >= self.src_start and n < self.src_start + self.range
    
    def get_dest(self, n):
        offset = n - self.src_start
        return self.dest_start + offset
    
class Table:
    def __init__(self, table_lines):
        #print(f'Creating table: {table_lines}')
        self.parse_name(table_lines[0])
        self.parse_rules(table_lines[1:])
    
    def parse_name(self, name_line):
        name_splits = name_line.split()[0].split('-')
        self.src = name_splits[0]
        self.dest = name_splits[2]

    def parse_rules(self, rule_lines):
        self.rules = []
        for rule_line in rule_lines:
            self.rules.append(Rule(rule_line))
    
    def get_output(self, n):
        for rule in self.rules:
            if rule.fits(n):
                return rule.get_dest(n)
        return n

class Almanach:
    def __init__(self, input_lines):
        #print(f'Creating Almanach: {input_lines}')
        self.parse_seeds(input_lines[0])
        self.parse_tables(input_lines[2:])
    
    def parse_seeds(self, seeds_line):
        seeds_part = seeds_line.split(':')[1].strip()
        self.seeds = [int(x) for x in seeds_part.split()]

    def parse_tables(self, tables_lines):
        self.tables = []
        current_table = []
        for line in tables_lines:
            if len(line) > 1:
                current_table.append(line)
                continue
            self.tables.append(Table(current_table))
            current_table = []
        self.tables.append(Table(current_table))
    
    def get_table_for_src(self, src):
        for table in self.tables:
            if table.src == src:
                return table
        return None
    
    def track_seed_to_location(self, seed):
        current_input = seed
        current_src = 'seed'
        current_table = self.get_table_for_src(current_src)
        
        while True:
            if not current_table:
                return (seed, current_input)
            current_input = current_table.get_output(current_input)
            current_src = current_table.dest
            current_table = self.get_table_for_src(current_src)

    def track_seeds_to_location(self):
        res = {}
        for seed in self.seeds:
            mapping = self.track_seed_to_location(seed)
            res[mapping[0]] = mapping[1]

        return res
    
    def track_seed_pairs_to_location(self):
        no = 1
        current_min = sys.maxsize
        for i in range(0,len(self.seeds),2):
            for seed in range(self.seeds[i], self.seeds[i] + self.seeds[i+1]):
                mapping = self.track_seed_to_location(seed)
                if current_min > mapping[1]:
                    current_min = mapping[1]
                
                print(f'[{i}/{len(self.seeds)//2}] {no} - current min: {current_min}')
                no +=1


with open('./input.txt', "r") as file:
    almanach = Almanach(file.readlines())
    print(min(almanach.track_seeds_to_location().values()))

    #Uncomment this to run the code for the second star
    #However it runs for ages, finally i used this code https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p2.py to get the solution
    #I was lazy/busy to come up with any types of optimizations
    # almanach.track_seed_pairs_to_location()