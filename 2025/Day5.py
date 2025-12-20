import os
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
                fresh_ids.append(line)
            else:
                ids.append(line)

    return fresh_ids, ids

def part1():
    fresh_ids, ids = load_data()
    fresh_dict = dict.fromkeys(fresh_ids)
    



def main():
    fresh_ids, ids = load_data()
    print(f"Fresh IDs: {fresh_ids}")
    print(f"Used IDs: {ids}")

if __name__ == "__main__":
    main()
    