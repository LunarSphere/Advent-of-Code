import os
import math #need eucleidean distance

#ref  https://youtu.be/Rd7c4Wx7QDg?si=Wk7QljKqJGlUeVVZ
# https://www.geeksforgeeks.org/dsa/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
# genuienly had no clue how to approach this one 
# leanred a lot from the video and geeksforgeeks article above
def load_data():
    with open(os.path.join("inputs", "day8.txt"), "r") as file:
        data = [line.strip().split("," ) for line in file]
        data = [list(map(int, line)) for line in data] #convert to integers
    return data

def part1():
    data = load_data()
    #create a list of all possible index pairs
    index_pairs = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            index_pairs.append((i, j))
    index_pairs.sort(key=lambda pair: math.dist(data[pair[0]], data[pair[1]])) #you can sort a list by using a custom key function neat!
    # so now we know the closest pairs
    #disjoined sets problem
    parent = [i for i in range(len(data))]
    # each circuit intiially just points to itself
    # parent[i] # the parent node of the node with index I 

    def root(x):
        #recursively find root of tree
        if parent[x] == x: return x
        #use path compression to get from deep tree to root faster 
        # ex instead of chaining just move deep node to be a child of root
        parent[x] = root(parent[x])
        return parent[x]
    
    def merge(a,b):
        # find root of tree a and make it a child of b
        parent[root(a)] = root(b) #rootb instead of b will ensure it moves to the root of parent not a child. 
    
    for a,b in index_pairs[:1000]:
        merge(a,b)
    # print(parent)

    # visualize the disjoined sets
    # for i in range(len(data)):
    #     print(f"Node {i} is in set with root {root(i)}")


    sizes = [0] * len(data) 
    for i in range(len(data)):
        sizes[root(i)] += 1 #count size of each set
    
    
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2] # product of sizes of 3 largest circuits

def part2():
    data = load_data()
    #create a list of all possible index pairs
    index_pairs = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            index_pairs.append((i, j))
    index_pairs.sort(key=lambda pair: math.dist(data[pair[0]], data[pair[1]])) #you can sort a list by using a custom key function neat!
    # so now we know the closest pairs
    #disjoined sets problem
    parent = [i for i in range(len(data))]
    # each circuit intiially just points to itself
    # parent[i] # the parent node of the node with index I 

    def root(x):
        #recursively find root of tree
        if parent[x] == x: return x
        #use path compression to get from deep tree to root faster 
        # ex instead of chaining just move deep node to be a child of root
        parent[x] = root(parent[x])
        return parent[x]
    
    def merge(a,b):
        # find root of tree a and make it a child of b
        parent[root(a)] = root(b) #rootb instead of b will ensure it moves to the root of parent not a child. 
    

    circuits = len(data)
    for a,b in index_pairs:
        if root(a) == root(b): continue #if already merged skip
        merge(a,b)
        circuits -= 1 
        if circuits == 1: #once we have a single circuit 
            return(data[a][0] * data[b][0]) #return product of their x coordinates 


def main():
    print("Advent of Code - Day 8")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()