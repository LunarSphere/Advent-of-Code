import os
def load_data(keep_str = False):

    data = []
    with open(os.path.join("inputs", "Day6.txt")) as f:
        lines = f.readlines()
        last = lines[-1]
        for line in lines:
            row = []
            if line != last:
                for num in line.strip().split():
                    if keep_str:
                        row.append(num)
                    else:
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
    data_t = []
    for i in range(len(data[0])):
        vert = []
        for j in range(len(data)):
            vert.append(data[j][i])
        data_t.append(vert)
    # print(len(data_t))
    # do calculations
    grand_total = 0
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
    data = load_data(keep_str=True)
    # data_t = list(zip(*data)) ## pythonic way to do the foor loop below but its less readable
    # print(data)
    #transpose data so its easier to iterate through
    data_t = []
    for i in range(len(data[0])):
        vert = []
        for j in range(len(data)):
            vert.append(data[j][i])
        data_t.append(vert)
    print(data_t)

    return

def main():
    
    print(part1())
    print(part2())
    # print(part2())
    # print(part1())
    # result1 = part1()
    # result2 = part2()
    # print(f"Part 1: {result1}")
    # print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()