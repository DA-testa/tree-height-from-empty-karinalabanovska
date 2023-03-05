# python3

import sys
import threading

def compute_height(n, parents):
    tree = [[] for i in range(n)]
    root = None

    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    stack = [(root, 1)]
    max_height = 0
    while stack:
        node, height = stack.pop()
        if not tree[node]:

            max_height = max(max_height, height)
        else:
            for child in tree[node]:
                stack.append((child, height+1))

    return max_height

def main():
    # n = int(input())
    # parents = list(map(int, input().split()))

    # print(compute_height(n, parents))
    
    mode = input()
    if "F" in mode:
        filename = input()
        if "a" not in filename:
            with open (str("test/"+filename), mode = "r") as f:
                n = int(f.readline())
                parentOfNode = list(map(int, f.readline().split()))
        
        else:
            print("error")
    elif "I" in mode:
        n = int(input())
        parentOfNode = list(map(int, input().split()))
    else:
        print("invalid mode")
    print(compute_height(n, parentOfNode))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

threading.Thread(target=main).start()
