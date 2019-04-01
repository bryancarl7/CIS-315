#           Assignment 2            #
# CIS 315 - Intermediate Algorithms #
#      Developer: Bryan Carl        #

# Brief Description: #

# For  this  assignment, you are to write a program which will take the
# description of a weighted directed acyclic graph from standard input
# and write to standard output two numbers measuring the graph.
# The program will need to compute (i) the length of the longest path
# from 1 to n, and(ii) the number of distinct paths from 1 to n that have
# the longest length found in part (i).

# Implementation #

# For my implementation, I made a graph class with a few variables for holding
# data about the structure, and I ended up using an adjacency matrix for my solution.
# Below in the calcLongestPath function is where I implemented my algorithm.
# It should be linear time. At the bottom is my "main" function, where I take standard
# input to create the graph implementation.

# To run this program #
# To Run this program, simply type

#   python3 DAG.py inSample.txt

# into a terminal with the correct working directory and it should take
# whatever input is in inSample.txt! email me if you have questions: bcarl@uoregon.edu
from collections import defaultdict
import fileinput


# Make Graph class to build
class Graph:
    def __init__(self, vertices):
        self.edgeList = []
        self.weights = {}
        self.vertexes = vertices
        self.topologicalSorted = []
        self.maxPaths = 0

        # Purely for topological sort
        self.graph = defaultdict(list)

    def addconnection(self, first, second, weight):
        # Setup Strings to implement weight dictionary
        s1 = str(first)
        s2 = str(second)
        s3 = s1+s2
        connect = {s3: weight}

        # append the edge numbers to adjacency list
        self.edgeList.append((first, second))
        self.weights.update(connect)

    def calcLongestPath(self):
        # Get Structures up and going
        n = len(self.topologicalSorted)-1
        LP = self.topologicalSorted.copy()
        NP = self.topologicalSorted.copy()

        # Initialize the arrays to have all -inf's
        LP[0] = 0
        NP[0] = 1
        for k in range(1, n+1):
            LP[k] = float("-inf")
            NP[k] = float("-inf")

        # Traverse edgelist and weights using double for loop
        for i in range(0, n):

            for j in range(i+1, n+1):
                # need to increment them because the indexes are behind the vertex #'s
                first = i + 1
                second = j + 1

                if (first, second) in self.edgeList:
                    # concatenate first and second string for easy lookup
                    weight = str(first)+str(second)

                    # Decide what to do based on weights/other vertices
                    if LP[i] + self.weights.get(weight) > LP[j]:
                        LP[j] = LP[i]+self.weights.get(weight)
                        NP[j] = NP[i]
                    elif LP[i] + self.weights.get(weight) == LP[j]:
                        NP[j] += NP[i]

        print("longest path: " + str(LP[n]))
        print("number of longest paths: " + str(NP[n]))

    # Again, purely for topological sort
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortRecursive(self, vertex, seen, list):
        seen[vertex-1] = True

        for i in self.graph[vertex]:
            if seen[i-1] is False:
                self.topologicalSortRecursive(i, seen, list)

        list.insert(0, vertex)

    def topologicalSort(self):
        seen = [False]*self.vertexes

        for item in range(1, self.vertexes):
            if seen[item] is False:
                self.topologicalSortRecursive(item, seen, self.topologicalSorted)


if __name__ == "__main__":
    # loop to initialize graph
    for line in fileinput.input():
        newline = line.split(" ")
        if len(newline) < 3:
            if newline[0] == "\n":
                break
            lines = newline[1]
            g = Graph(int(newline[0]))
            continue
        # Actually adds them to the graph
        g.addEdge(int(newline[0]), int(newline[1]))
        g.addconnection(int(newline[0]), int(newline[1]), int(newline[2]))
    # Functions to additional sort out graph
    g.topologicalSort()
    g.calcLongestPath()
