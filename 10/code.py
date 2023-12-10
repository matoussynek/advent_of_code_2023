from enum import Enum

class Directions(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

class Node:
    def __init__(self, c):
        self.symbol = c
        self.update_outputs(c)
    
    def update_outputs(self, c):
        if c == '.':
            self.outputs = [False, False, False, False]
        elif c == '|':
            self.outputs = [True, False, True, False]
        elif c == '-':
            self.outputs = [False, True, False, True]
        elif c == 'L':
            self.outputs = [True, True, False, False]
        elif c == 'J':
            self.outputs = [True, False, False, True]
        elif c == '7':
            self.outputs = [False, False, True, True]
        elif c == 'F':
            self.outputs = [False, True, True, False]
        else:
            self.outputs = [True, True, True, True]
    
    def has_input(self, i):
        return self.outputs[i]
    
    def get_outputs(self, i):
        outputs = []
        for j in range(4):
            if i == j:
                continue
            if self.outputs[j]:
                if j == 0:
                    outputs.append((2,(0,-1)))
                elif j == 1:
                    outputs.append((3,(1,0)))
                elif j == 2:
                    outputs.append((0,(0,1)))
                else:
                    outputs.append((1,(-1,0)))
        return outputs
    
class Map:
    def __init__(self, lines):
        self.nodes = []
        self.start_position = None
        self.parse_lines(lines)

    def parse_lines(self, lines):
        for y, line in enumerate(lines):
            line_nodes = []
            for x, c in enumerate(line):
                node = Node(c)
                line_nodes.append(node)
                if c == 'S':
                    self.start_position = (x,y)
            self.nodes.append(line_nodes)
    
    def get_node(self, pos):
        return self.nodes[pos[1]][pos[0]]
    
    def get_position(self, current, dir):
        return (current[0]+dir[0], current[1]+dir[1])
    
    def star1(self):
        found_nodes = []
        current_position = self.start_position
        current_node = self.get_node(current_position)
        last_input = 2
        while True:

            if len(found_nodes) > 0 and current_position == self.start_position:
                break

            print('im at:', current_node.symbol)

            possible_outputs = current_node.get_outputs(last_input)
            for possible_input, possible_output in possible_outputs:
                possible_node = self.get_node(self.get_position(current_position, possible_output))
                if possible_node.has_input(possible_input):
                    current_node = possible_node
                    found_nodes.append(possible_node)
                    current_position = self.get_position(current_position, possible_output)
                    last_input = possible_input
                    break
        
        print(f'Max distance: {len(found_nodes)//2}')


    
map = Map(open('./input.txt').readlines())
map.star1()

#Wont bother with star2... No time
