# python3

import sys
import threading

def compute_height(n, parents):
    # Create an array to represent the tree where each index represents a node and its value is the parent of that node
    tree = [[] for i in range(n)]
    root = None

    # Build the tree
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    # Traverse the tree using DFS with a stack to calculate the height of the tree
    stack = [(root, 1)]
    max_height = 0
    while stack:
        node, height = stack.pop()
        if not tree[node]:
            # Leaf node
            max_height = max(max_height, height)
        else:
            for child in tree[node]:
                stack.append((child, height+1))

    return max_height

def main():
    n = int(input())
    parents = list(map(int, input().split()))

    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

threading.Thread(target=main).start()
