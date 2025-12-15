import os

def read_file() -> list:
    filename = os.path.join("inputs", "Day1.txt")
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def part1() -> int:
    dial = 50
    zero_count = 0
    rotations = read_file()
    for rotate in rotations:
        direction = rotate[0]
        count = int(rotate[1::])#separate the number of rotations from the direction and conver to int
        #move dial
        for r in range(count):
            if direction == "L":
                dial-=1
            else:
                dial+=1
            dial = dial % 100 # ensure dial is in 0-99 range
        if dial == 0:
            zero_count+=1
    return zero_count
def part2() -> int:
    dial = 50
    zero_count = 0
    rotations = read_file()
    for rotate in rotations:
        direction = rotate[0]
        count = int(rotate[1::])#separate the number of rotations from the direction and conver to int
        #move dial
        for r in range(count):
            if direction == "L":
                dial-=1
            else:
                dial+=1
            dial = dial % 100 # ensure dial is in 0-99 range
            if dial == 0:
                zero_count+=1
    return zero_count
    

def main():
    print(f"the password is {part1()}")
    print(f"the password is {part2()}")

if __name__ == "__main__":
    main()
