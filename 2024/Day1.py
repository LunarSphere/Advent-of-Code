
def solve_part1():
    ### SOLUTION 3574690 ###
    list1 = [] #left side 
    list2 = [] #right side
    #turn txt into 2 lists
    file = open("input/day1.txt", "r")
    lines = file.readlines()
    file.close()
    total_distance = 0
    for line in lines:
        if line.split(" "):
            list1.append(int(line.strip().split()[0]))
            list2.append(int(line.strip().split()[1]))
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        total_distance+= abs(list1[i] - list2[i])
    return total_distance

def solve_part2():
    ### SOLUTION 22565391  ###
    list1 = [] #left side
    list2 = [] #right side
    dict1 = {} 
    # turn txt into 2 lists
    file = open("input/day1.txt", "r")
    lines = file.readlines()
    file.close()
    similarity = 0
    for line in lines:
        if line.split(" "):
            list1.append(int(line.strip().split()[0]))
            list2.append(int(line.strip().split()[1]))
    list1.sort()
    list2.sort()
    ## Make a dictionary with number as a key and each time it appears in right list. Number must be present in list 1
    for i in range(len(list2)):
        if list2[i] in dict1.keys():
            dict1[list2[i]] +=1
        else:
            dict1[list2[i]] = 1
    for i in set(list1):
        if i in dict1.keys():
            similarity += i * dict1[i]
    return similarity

def main():
    print(solve_part1())
    print(solve_part2())
    return 0 

if __name__ == "__main__":
    main()
