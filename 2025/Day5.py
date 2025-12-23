import os

### references
#https://www.geeksforgeeks.org/dsa/merging-intervals/

def load_data():
    fresh_ids = []
    ids = []
    #read fresh ids until empty line then read used ids
    with open(os.path.join("inputs", "Day5.txt"), "r") as file:
        lines = file.readlines()
        reading_fresh = True
        for line in lines:
            line = line.strip()
            if line == "":
                reading_fresh = False
                continue
            if reading_fresh:
                range_ = [int(line.split("-")[0]), int(line.split("-")[1])]
                fresh_ids.append(range_)
            else:
                ids.append(int(line))

    return fresh_ids, ids

def part1():
    fresh_ids, ids = load_data()
    valid_ids = []
    for i, id in enumerate(ids):
        for fresh_r in fresh_ids:
            if id >= fresh_r[0] and id <= fresh_r[1]:
                valid_ids.append(id)
                break
    return (len(valid_ids))

def merge_intervals(ids):
    ids.sort()
    merged = []
    merged.append(ids[0])

    for i in range(1, len(ids)):
        last = merged[-1]
        curr = ids[i]

        #if current interval overalps with last merged interval merge them
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            merged.append(curr)
    return merged

def part2():
    fresh_ids, ids = load_data()
    p_valid_ids = []
    total_potential_ids = 0
    fresh_ids = merge_intervals(fresh_ids)
    for fresh_r in fresh_ids:
        total_potential_ids += (fresh_r[1] - fresh_r[0]) + 1
    return total_potential_ids


    



def main():
    print(f"🎅Advent of Code Day 5🎅\n")
    fresh_ids, ids = load_data()
    print(f"In part 1 {part1()} of the availible ingredient IDs are fresh!")
    print(f"In part 2 {part2()} ingredient IDs are considered to be fresh!")
if __name__ == "__main__":
    main()
    