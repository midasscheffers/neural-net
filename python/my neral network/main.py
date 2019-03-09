import numpy as np
from node import *
import random as r

def generate_rand_weights(nummber_of_items):
    rand_list = []
    for i in range(nummber_of_items):
        rand_list.append(r.random())
    return rand_list

nummber_of_inp_nodes = 20

inp_nodes = []

for i in range(nummber_of_inp_nodes):
    n = Node([], [], r.uniform(-10, 10))
    inp_nodes.append(n)

n1 = Node(inp_nodes, generate_rand_weights(nummber_of_inp_nodes), 0)
n2 = Node(inp_nodes, generate_rand_weights(nummber_of_inp_nodes), 0)

n1.calc_output()
n2.calc_output()

n3 = Node([n1, n2], [1,-1], 0)

n3.calc_output()