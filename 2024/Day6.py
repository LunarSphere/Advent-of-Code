# I would say the core skill learned here is more matrix navigation?
def load_data():
    data = []
    with open("input/day6.txt", "r") as file:
        for line in file.readlines():
            data.append(list(line.strip()))  
    file.close()                      
    return data

def solve(data=None):
    ## Part one:
    ## Rule: if something in front turn right 90 degrees 
    ## Rule: else step forward
    # mark stepped on spots with X to count at the end
    # reaching a bound  terminates loop
    if data is None:
        data = load_data()

    sum_X = 0
    loop = 0
    visited = set()
    # find position of guard
    guard_pos = []
    for r in range(len(data)):
        for c in range(len(data[r])):
        #multi type lists are a sin
        #position and angle facing
            if data[r][c] == "^":
                guard_pos = [r,c, 0]
            elif data[r][c] == ">":
                guard_pos = [r, c, 90]
            elif data[r][c] == "<":
                guard_pos = [r,c, 270]
            elif data[r][c] == "v":
                guard_pos = [r,c, 180]
            

    
    # simulate guards route 
    while((guard_pos[0] > 0 and guard_pos[1] >0) and guard_pos[0] < len(data)-1 and guard_pos[1] < len(data[0]) -1):
        # get guards rown and column
        r = guard_pos[0]
        c = guard_pos[1]
        # each if/elif is same check but on a different orientation
        if guard_pos[2] == 0:
            # 0 degrees 
            # if position in front is blocked
            if data[r-1][c] == "#":
                # rotate & update orientation(angle facing)
                data[r][c] = ">"
                guard_pos = [r,c, 90]
            else: 
                # else move forward maintain orientation
                data[r][c] = "X"
                data[r-1][c] = "^"
                guard_pos = [r-1, c, 0]
        #rinse and repeat
        elif guard_pos[2] == 90:
            if data[r][c+1] == "#":
                data[r][c] = "v"
                guard_pos = [r,c, 180] 
            else: 
                data[r][c] = "X"
                data[r][c+1] = ">"
                guard_pos = [r,c+1, 90]
        elif guard_pos[2] == 180:
            if data[r+1][c] == "#":
                data[r][c] = "<"
                guard_pos = [r,c, 270] 
            else: 
                data[r][c] = "X"
                data[r+1][c] = "v"
                guard_pos = [r+1,c, 180]

        elif guard_pos[2] == 270:
            if data[r][c-1] == "#":
                data[r][c] = "^"
                guard_pos = [r,c, 0] 
            else: 
                data[r][c] = "X"
                data[r][c-1] = "<"
                guard_pos = [r,c-1, 270]

        if tuple(guard_pos) in visited:
            loop = 1
            break
        else:
            visited.add(tuple(guard_pos))


    data[guard_pos[0]][guard_pos[1]] = "X" # mark the final position

    for r in data:
        sum_X+= r.count("X")
    return sum_X, loop


##part 2 
# place an additional object in each potential position and see which ones would cause a looop. 
# defined by if guard returns to start with same initial direction. 
#1609
def solve2():
    loops = 0
    data = load_data() # initial loading of data
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] != "#" and data[r][c] not in "^><v":
                data_temp = [r[:] for r in data]
                data_temp[r][c] = "#"
                sumX, loop = solve(data_temp)
                loops+=loop
    return loops



def main():
    print(solve())
    print(solve2())

if __name__ == "__main__":
    main()