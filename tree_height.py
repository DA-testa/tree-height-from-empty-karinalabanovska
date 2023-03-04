# python3

import sys
import threading

def compute_height(n, parents):
    # create an array to store the height of each node, initialized to 0
    heights = [0] * n
    
    # iterate over each node
    for i in range(n):
        # if the height of the node hasn't been computed yet
        if heights[i] == 0:
            # calculate the height of the node and its ancestors
            height = 1
            parent = parents[i]
            while parent != -1:
                if heights[parent] != 0:
                    # if the height of the parent has already been computed,
                    # use that to calculate the height of this node
                    height += heights[parent]
                    break
                height += 1
                parent = parents[parent]
            # store the height of the node in the array
            heights[i] = height
    
    # return the maximum height
    return max(heights)

def main():
    # read input from standard input or files
    if len(sys.argv) == 1:
        # read input from standard input
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        # read input from file
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    
    # compute the height of the tree
    height = compute_height(n, parents)
    
    # output the result
    print(height)

# Increase the recursion limit and stack size for large trees
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
