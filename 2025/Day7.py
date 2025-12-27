import os
from functools import lru_cache

def load_data():
    with open(os.path.join("inputs", "Day7.txt")) as f:
        data = [list(line.strip("\n")) for line in f]
    return data

def part1():
    data = load_data()
    splits = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == "S":
                if r+1 < len(data):
                    if  data[r+1][c] == "^":
                        splits += 1
                        data[r+1][c-1] = "|"
                        data[r+1][c+1] = "|"
                    else:
                        data[r+1][c] = "|" 
            if data[r][c] == "|":
                if r+1 < len(data):
                    if r+1 < len(data) and data[r+1][c] == "^":
                        splits += 1
                        data[r+1][c-1] = "|"
                        data[r+1][c+1] = "|"
                    else:
                        data[r+1][c] = "|"
    #visualize
    # for row in data:
    #     print("".join(row))
    return splits


@lru_cache(maxsize=None) #if a function is called with same arguments again it returns whats previously calculated
def dp(r, c) -> int:
    """
    ##Refrence
    ##https://yordi.me/advent-of-code-2025-day-7/

    uses dynamic programming to figure out the potential paths for the tachyon

    input start row and col
    if r >= len of the data we've reached the end of a path so return 1
    other wise depending on split or nothing call dp with the updated coordinate. 
    lru cache stores previously traveresed paths to prevent the recursive funciton from recalculating paths
    
    r: row 
    :c: column
    :return: returns total number of quantum paths
    :rtype: int
    """

    data = load_data()
    #we've reached the end of a path
    if r >= len(data):
        return 1
    #if ^ call for left and right path 
    if data[r][c] == '^':
        return dp(r, c - 1) + dp(r, c + 1)
    #if no split call straight down
    else:
        return dp(r + 1, c)

def dp_mine(r, c, memo={}) -> int:
    """
    ##Refrence
    ##https://yordi.me/advent-of-code-2025-day-7/

    my version w/o lru_cache 
    just use a dictionary to store the previous results
    r: row 
    :c: column
    :return: returns total number of quantum paths
    :rtype: int
    """

    data = load_data()
    #we've reached the bottom of a path so return 1
    if (r,c) in memo:
        return memo[(r,c)]
    if r >= len(data):
        return  1
    #if ^ call for left and right path until bottom
    if data[r][c] == '^':
        result =  dp_mine(r, c - 1) + dp_mine(r, c + 1)
    #if no split dp but we do straight down until bottom
    else:
        result =  dp_mine(r + 1, c)
    memo[(r,c)] = result #store previous results in a dictionary for reference
    return result

def part2():
    data = load_data()
    start_col = 0
    #find starting column
    for c in range(len(data[0])):
        if data[0][c] == "S":
            start_col = c
    #look for potential "quantum" paths recursively
    total_paths = dp_mine(0, start_col)
    return total_paths
    

def main():
    print("!!! Advent of Code 2025 DAY 7 !!!")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()