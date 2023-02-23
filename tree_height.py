# python3

import sys
import threading
# import numpy


def compute_height(n, parents):
    max_height = 0
    for i in range(n-1):
        height = 1
        var = parents[i]
        while var != -1:
            var = parents[var]
            print("Parents i:", parents[i])
            height += 1
        if max_height < height:
            max_height = height
    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if 'I' in text:
        n = int(input("Number of elements: "))
        parents = [int(x) for x in list(input("Parents:").split())]
        print("Parents: ", parents, "Elements: ", n)
        print("Parents: ", parents[0])
    if 'F' in text:
        filename = input()
        filename = "./test/" + filename        
        with open(filename, mode="r") as fails:
            text = fails.readline()
            parents = [int(x) for x in list(input("Parents:").split())]
            print("Lasamais fails: ", text)

    print("Max height: ", compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
