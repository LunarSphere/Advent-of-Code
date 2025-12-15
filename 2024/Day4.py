# OMNI directional brute force Search
def search(y,x, dx, dy, key = "XMAS") -> bool:
    # returns true or false depending on if key is present
    #load the matrix
    matrix = []
    file = open("input/day4.txt")
    for line in file.readlines():
        r = [c for c in line if c != "\n"]
        matrix.append(r)
    # maximum bound of x or y
    extentX = x + (dx*(len(key)-1))
    extentY = y + (dy*(len(key)-1))
    # if less than or greater than bound quit
    if extentX < 0 or extentY < 0 or extentX >= len(matrix[0]) or extentY >= len(matrix):
        return False
    # keep checking for matching letters else return false
    for i, k in enumerate(key):
        new_x = x + (i*dx)
        new_y = y + (i*dy)
        if matrix[new_y] [new_x] != k:
            return False
    # if it finishes its a match
    return True


def part1() -> int: #ans: 2427
    # for word at at each position i,j in array. if its present increase the count
    # load data into a 2darray
    matrix = []
    file = open("input/day4.txt")
    for line in file.readlines():
        r = [c for c in line if c != "\n"]
        matrix.append(r)
    file.close()


    count = 0
    # check up,down,left,right, up-right, down-right, up left, down-left 
    #search each character in every direction
    for y in range(len(matrix)):
        for x in range(len(matrix[y])): 
            if search(y,x,0,1): count+=1 # search right
            if search(y,x,0,-1): count +=1 #search left
            if search(y,x,-1,0): count+=1 # search up
            if search(y,x,1,0): count +=1 # search down
            if search(y,x,-1,1): count+=1 #search up right
            if search(y,x,-1,-1): count +=1 #search upleft
            if search(y,x,1,1): count+=1 #search down right
            if search(y,x,1,-1): count +=1 #search down left
    return count

def part2(): #ans = 1900
    #we are looking for MAS in the shape of an X A is always in the center. 
    # check for x-mas for every a in matrix
    # there are 4 possible orientations that you can get by taking any position and rotaiting 4 times.
    matrix = []
    file = open("input/day4.txt")
    for line in file.readlines():
        r = [c for c in line if c != "\n"]
        matrix.append(r)
    file.close()
    count = 0
    # check up,down,left,right, up-right, down-right, up left, down-left 
    #search each character in every direction
    for y in range(len(matrix)):
        for x in range(len(matrix[y])): 
            if matrix[y][x] == "A":
                if search(y,x,-1,-1, "AM") and  search(y,x,-1,1, "AS") \
                and search(y,x,1,-1, "AM") and search(y,x,1,1, "AS"): count +=1 # Check orientation 1
                
                if search(y,x,-1,-1, "AS") and  search(y,x,-1,1, "AM") \
                and search(y,x,1,-1, "AS") and search(y,x,1,1, "AM"): count +=1 # Check orientation 2

                if search(y,x,-1,-1, "AM") and  search(y,x,-1,1, "AM") \
                and search(y,x,1,-1, "AS") and search(y,x,1,1, "AS"): count +=1 # Check orientation 3

                if search(y,x,-1,-1, "AS") and  search(y,x,-1,1, "AS") \
                and search(y,x,1,-1, "AM") and search(y,x,1,1, "AM"): count +=1 # Check orientation 4
    return count


def main():
    print(part1())
    print(part2())
    return

if __name__ == "__main__":
    main()