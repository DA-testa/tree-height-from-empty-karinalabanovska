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

    # Traverse the tree using DFS to calculate the height of the tree
    def dfs(node, height):
        nonlocal max_height
        if not tree[node]:
            # Leaf node
            max_height = max(max_height, height)
            return
        for child in tree[node]:
            dfs(child, height+1)

    max_height = 0
    dfs(root, 1)
    return max_height

def main():
    # Read input values
    n = int(input())
    parents = list(map(int, input().split()))

    # Compute and output the height of the tree
    print(compute_height(n, parents))

# Set the recursion limit and stack size for the main thread
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

# Start the main thread
threading.Thread(target=main).start()
