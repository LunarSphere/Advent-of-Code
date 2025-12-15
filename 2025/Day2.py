import os
import re

def read_file() -> list:
    with open(os.path.join("inputs","Day2.txt"), "r") as file:
        for line in file:
            return line.split(",")

def part1() -> int:
    ranges = read_file()
    invalid_total = 0

    for range_ in ranges:
        
        start = int(range_.split("-")[0]) #split "-" to sepearate 11 & 22 "11-22" 
        stop =  int(range_.split("-")[1])
        #for every number in the range see if first half equals second half
        for num in range(start,stop+1):
            if str(num)[:len(str(num))//2] == str(num)[len(str(num))//2:]:
                invalid_total+=num
    print(invalid_total)

def part2() -> int:
    ranges = read_file()
    invalid_total = 0

    for range_ in ranges:
        
        start = int(range_.split("-")[0]) #split "-" to sepearate 11 & 22 "11-22" 
        stop =  int(range_.split("-")[1])
        #for every number in the range see if first half equals second half
        for num in range(start,stop+1):
            if bool(re.fullmatch(r"^(\d+)\1+$", str(num))): # this regex expression identifies repeating groups like 123 in 123123123
                invalid_total+=num
    print(invalid_total)


def main():
    print("🎄 Day 2 Advent of Code 2025 🎄")
    part1()
    part2()

if __name__ == "__main__":
    main()
