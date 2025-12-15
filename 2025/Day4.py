import os
def load_data() -> list[str]:
    with open(os.path.join("inputs", "Day4.txt"), "r") as f:
        data = [list(line.strip()) for line in f]
    return data

def part1() -> int:
    #check each @ in all 8 directions to determine if their are less than 
    #4 rolls of tp in 8 adjacent positions
    data = load_data()
    #  [] directions: N, NE, E, SE, S, SW, W, NW
    accessible_rolls=0
    omni_directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for y in range(len(data)):
        for x in range(len(data[y])):
            #check each roll
            if data[y][x] == "@": 
                adj_roll_count = 0
                #check all 8 directions for a roll
                for dx, dy in omni_directions:
                    if (y+dy >= 0 and x+dx >= 0 and y+dy < len(data) and x+dx < len(data[y])):
                        if data[y+dy][x+dx] == "@":
                            adj_roll_count+=1
                if adj_roll_count < 4:
                    accessible_rolls+=1
    return accessible_rolls            
                    
def remove_rolls(data):
    accessible_rolls=0
    omni_directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for y in range(len(data)):
        for x in range(len(data[y])):
            #check each roll
            if data[y][x] == "@": 
                adj_roll_count = 0
                #check all 8 directions for a roll
                for dx, dy in omni_directions:
                    if (y+dy >= 0 and x+dx >= 0 and y+dy < len(data) and x+dx < len(data[y])):
                        if data[y+dy][x+dx] == "@":
                            adj_roll_count+=1
                if adj_roll_count < 4:
                    data[y][x] = "x"
                    accessible_rolls+=1
    return accessible_rolls, data 

def part2():
    # utilize the finding algorithim from part 1 
    # but check if new rollls can be pruned after previous prune
    total_accessible_rolls = 0
    data = load_data()
    while True:
        accessible_rolls, data = remove_rolls(data)
        total_accessible_rolls += accessible_rolls
        if accessible_rolls == 0:
            break 
    return total_accessible_rolls








def main():
    print(f"🎅Advent of Code Day 4🎅\n")
    print(f"There are {part1()} accessible rolls of toilet paper for part 1 \n")
    print(f"There are {part2()} accessible rolls of toilet paper for part 2 \n")
    # data = load_data()
    # print(f"Loaded\n {data}")
    

if __name__ == "__main__":
    main()