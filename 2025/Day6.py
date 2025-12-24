import os

def load_data(keep_str = False):
    data = []
    with open(os.path.join("inputs", "Day6.txt")) as f:
        lines = f.readlines()
        last = lines[-1]
        for line in lines:
            row = []
            if line != last:
                if keep_str:
                    for num in line.split():
                        row.append(num)
                else:
                    for num in line.strip().split():
                        row.append(int(num))
                data.append(row)
            else:
                data.append(line.strip().split())
    return data


def part1():
    data = load_data()
    # data_t = list(zip(*data)) ## pythonic way to do the foor loop below but its less readable
    # print(data)
    #transpose data so its easier to iterate through
    #gives a list of each number then their operation as last digit
    data_t = []
    for i in range(len(data[0])):
        vert = []
        for j in range(len(data)):
            vert.append(data[j][i])
        data_t.append(vert)
    # print(len(data_t))
    # do calculations
    grand_total = 0
    #depending on the operator go through a loop adding them together
    for eq in data_t:
        result_add = 0
        result_mult = 1 
        for i in range(0, len(eq)-1):
            if eq[-1] == '*':
                result_mult *= eq[i]
            if eq[-1] == '+':
                result_add += eq[i]
                result_mult = 0
        grand_total += result_add + result_mult               
        
    return grand_total
    


def part2():
    #format such that each column is its own list
    with open(os.path.join("inputs", "Day6.txt")) as f:
        data = [line.strip("\n") for line in f]
    # print(data)
    data_t = []
    for i in range(len(data[0])):
        vert = []
        for j in range(len(data)):
            vert.append(data[j][i])
        data_t.append(vert)
    # print(list(data_t))
    ##create groups
    # group is a list every list prior to an a list of all " "
    group = []
    groups = []
    for col in data_t:
        if set(col) == {" "}:
            groups.append(group)
            group = []
        else:
            group.append(col)
    #catch final group
    if group:
        groups.append(group)

    #calculate grad total by joining the lists into numbers and performing apprpriot operation
    grand_total = 0
    for group in groups:
        operator = group[0][-1]
        sum_ = 0 
        prod_ = 1
        for num in group:
            if operator == "+":
                sum_ += int(''.join(num[:-1]))
                prod_ = 0
            if operator == "*":
                prod_ *= int(''.join(num[:-1]))
        grand_total += prod_ + sum_
    
    return grand_total
        



        
def main():
    print("!!! Advent of Code 2025 DAY 6 !!!")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

if __name__ == "__main__":
    main()