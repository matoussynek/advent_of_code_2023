from math import gcd

class Node:
    def __init__(self, node_line):
        node_line = node_line.replace(" ","")
        self.name, rest = node_line.split('=')
        self.left, self.right = rest.replace('(','').replace(')','').strip().split(',')

    def get_next(self, dir):
        if dir == 'L':
            return self.left
        return self.right

class Map:
    def __init__(self, map_lines):
        self.nodes = {}
        self.parse_map(map_lines)

    def add_node(self, node_line):
        node = Node(node_line)
        self.nodes[node.name] = node
        return node

    def parse_map(self, map_lines):
        self.directions = map_lines[0].strip()
        map_lines = map_lines[2:]
        for i in range(0, len(map_lines)):
            self.add_node(map_lines[i])

    
    def traverse_map(self, start_node, end_node):
        current_node = self.nodes[start_node]
        steps = 0
        while (end_node and not current_node.name == end_node) or (not end_node and not current_node.name[2] == 'Z'):
            i = steps % len(self.directions)
            current_node = self.nodes[current_node.get_next(self.directions[i])]
            steps += 1

        print(f'Total steps: {steps}')
        return steps
    

    def star2(self):
        steps = []
        for k,node in self.nodes.items():
            if not k[2] == 'A':
                continue
            steps.append(self.traverse_map(k, None))
        
        lcm = 1
        for i in steps:
            lcm = lcm*i//gcd(lcm, i)
        print(f'Star 2 total steps: {lcm}')


map = Map(open('./input.txt').readlines())
map.traverse_map('AAA', 'ZZZ')
map.star2()

