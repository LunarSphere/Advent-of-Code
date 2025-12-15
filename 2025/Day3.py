import os
def load_data():
    with open(os.path.join(os.getcwd(),"inputs", "Day3.txt")) as f:
        return [line.strip() for line in f]
def part1() -> int:
    total_joltage = 0
    battery_banks = load_data()

    for bb in battery_banks:
        max_joltage = "00"
        #just make pairs with all the joltages and the biggest one is the max
        #i & j ensure ordering is consisternt
        for i in range(len(bb)):
            for j in range(i+1, len(bb)):
                joltage = bb[i] + bb[j]
                if int(joltage) > int(max_joltage):
                    max_joltage = joltage
        total_joltage+=int(max_joltage)
    return total_joltage
        
def part2():
    total_joltage = 0
    battery_banks = [[int(i) for i in bb] for bb in load_data()] #turn the loaded data into a list of integwers
    for bb in battery_banks:
        i_in = 0 
        joltage = ""
        # until no batteries remain
        for battries_left in range(11, -1, -1): 
            # find the largest batter
            i_in, largest = findLargest(bb, battries_left, i_in)
            joltage += str(largest) # update the joltage string
        total_joltage += int(joltage) #summ the totals
    return total_joltage    

def findLargest(bb, numbers_left, i_in):
    #helper function
    new_i = 0 # set new i to 0
    largest = -1 
    for i in range(i_in, (len(bb) - numbers_left)): # search for biggest number between start and len L - numbers left
        if (bb[i] > largest):  
            largest = bb[i]
            new_i = i+1 
    return new_i, largest 


def main():
    print(f"🎅Advent of Code Day 3🎅\n")
    print(f"The total ⚡joltage⚡ for part 1 is {part1()} \n")
    print(f"The total ⚡joltage⚡ for part 2 is {part2()} \n")
if __name__ == "__main__":
    main()