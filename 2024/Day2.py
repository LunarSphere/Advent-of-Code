def part1():
    file = open("input/day2.txt")
    lines = file.readlines()
    safereports = 0
    for line in lines:
        consistent = []
        consistentcheck = False
        safe = True
        #line by line creates a report that is a interger list. 
        report = [int(i) for i in line.split(" ")]
        for i, v in enumerate(report[:-1]):
            #check if the report is safe
            difference = v-report[i+1]
            #check if difference is greater than 3 or less than one
            if abs(difference) > 3 or  abs(difference) < 1:
                safe = False
                break
            consistent.append(difference/abs(difference))
        #check if all values are decreasing
        if all(n > 0 for n in consistent) or all(n < 0 for n in consistent): # had to look this up
            consistentcheck = True

        if safe and consistentcheck:
            safereports +=1
    return safereports


def issafe(report: list):
    signs = []
    safe = True
    consistentcheck = False
    for i, v in enumerate(report[:-1]):
            #check if the report is safe
            difference = v-report[i+1]
            #check if difference is greater than 3 or less than one
            if abs(difference) > 3 or  abs(difference) < 1:
                safe = False
                break
            signs.append(difference/abs(difference))
    #check if all values are decreasing
    if all(n > 0 for n in signs) or all(n < 0 for n in signs): # had to look this up
        consistentcheck = True
    if safe and consistentcheck:
        return True


def part2():
    file = open("input/day2.txt")
    lines = file.readlines()
    safereports = 0
    for line in lines:
        #line by line creates a report that is a interger list. 
        report = [int(i) for i in line.split(" ")]
        if issafe(report):
            safereports +=1
        # Had to look this up buy my solution of attempting to count each incorrect one was over thing the problem I just needed to skip an index and break
        else:
            for i in range(len(report)): # all I had to do was implement a condition for iterating through and skipping a number
                if issafe(report[:i] + report[i+1:]):
                    safereports +=1
                    break
                    
    return safereports

def main():
    print(part1())
    print(part2())
if __name__ == "__main__":
    main()