# python3

import sys
import threading
# import numpy as np


def compute_height(n, parents):
    max_height = 0
    for i in range(n-1):
        height = 1
        var = parents[i]
        while var != -1:
            var = parents[var]
            height += 1
        if max_height < height:
            max_height = height
    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if 'I' in text:
        n = int(input())
        parents = [int(x) for x in list(input().split())]
    if 'F' in text:
        filename = "./test/" + input()     
        with open(filename, mode="r") as fails:
        # with open("file.txt", mode="r") as fails:
            n = int(fails.readline())
            parents = fails.readline()
        parents = [int(x) for x in list(parents.split())]
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
