# python3

import sys
import threading

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []
        self.parent = None

def compute_height(n, parents):
    # Initialize an array of nodes
    nodes = [Node(i) for i in range(n)]
    
    # Construct the tree
    root_index = None
    for i in range(n):
        parent_index = parents[i]
        if parent_index == -1:
            root_index = i
        else:
            parent_node = nodes[parent_index]
            parent_node.children.append(nodes[i])
            nodes[i].parent = parent_node
            
    # Calculate the height of the tree
    height = 0
    nodes_at_current_level = [nodes[root_index]]
    while nodes_at_current_level:
        height += 1
        nodes_at_next_level = []
        for node in nodes_at_current_level:
            nodes_at_next_level.extend(node.children)
        nodes_at_current_level = nodes_at_next_level
    
    return height


def main():
    # Get user input for file name
    file_name = input("Enter file name: ")
    while 'a' in file_name:
        file_name = input("Invalid file name, enter a new one: ")

    # Read input from file
    with open(file_name, 'r') as f:
        n = int(f.readline())
        parents = list(map(int, f.readline().split()))

    # Calculate and output the height of the tree
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
