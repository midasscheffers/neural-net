import random as r
from node import *

class Network:

    def __init__(self, layers):
        self.layers = layers
        self.nodes = []

        for i in range(len(self.layers)):
            self.nodes.append([])
            
            for j in range(self.layers[i]):
                if i == 0:
                    n = Node([], [], r.uniform(-1,1))
                    self.nodes[i].append(n)
                else:
                    n = Node(self.nodes[i-1], self.generate_rand_weights(len(self.nodes[i-1])), 0)
                    self.nodes[i].append(n)


    def run(self):
        for i in range(len(self.nodes)):
            if i == 0:
                pass
            else:
                for j in range(len(self.nodes[i])):
                    print(self.nodes[i][j].calc_output(), j)

    def generate_rand_weights(self, nummber_of_items):
        rand_list = []
        for i in range(nummber_of_items):
            rand_list.append(r.uniform(-1,1))
        return rand_list
