# Getting REGEX using extracted values
import re
def part1():
    file = open("input/day3.txt")
    lines = file.readlines()
    uncorrupted_pattern = r"mul\(\d*\,\d*\)"
    digit_pattern = r"\d+"
    # is it possible to make a pattern to get the two numbers
    multiplied_total = 0
    for line in lines:
        muls = re.findall(uncorrupted_pattern, line)
        for mul in muls:
            multiples = re.findall(digit_pattern,mul)
            multiplied_total += int(multiples[0]) * int(multiples[1])
            
    file.close()
    return multiplied_total

def part2():
    file = open("input/day3.txt")
    lines = file.readlines()
    uncorrupted_pattern =r'mul\(\d*\,\d*\)|do\(\)|don\'t\(\)|"' 
    digit_pattern = r"\d+"
    do_or_dont = True
    # is it possible to make a pattern to get the two numbers
    multiplied_total = 0
    for line in lines:
        muls = re.findall(uncorrupted_pattern, line)
        for mul in muls:
            if mul == "do()":
                do_or_dont = True
            elif mul == "don't()":
                do_or_dont = False
            elif do_or_dont:
                multiples = re.findall(digit_pattern,mul)
                multiplied_total += int(multiples[0]) * int(multiples[1])
            
    file.close()
    return multiplied_total

def main():
    print(part1())
    print(part2())
    return 0

if __name__ == "__main__":
    main()