# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    max_height = 0
    if np.any(n) and np.any(parents):
        for i in range(n-1):
            height = 1
            var = parents[i]
            while var != -1:
                var = parents[var]
                height += 1
            if max_height < height:
                max_height = height
    else: 
        return max_height
    return max_height


def main():
    text = input()
    if 'I' in text:
        n = int(input())
        parents = list(map(int, input().split()))
        parents = np.array(parents)
    if 'F' in text:
        # filename = "./test/" + input()     
        # with open(filename, mode="r") as fails:
        with open("./test/05", mode="r") as fails:
            n = int(fails.readline())
            parents = fails.readline()
        parents = list(map(int, parents.split()))
        parents = np.array(parents)
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
