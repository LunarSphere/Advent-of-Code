# for this one for the actual input you just need to see if the area is big enough for all the sahpes to fit
# the example is np hard which is kinda funny
import os

def load_data():
    shape_dict = {}
    area_dict = {}
    with open(os.path.join("inputs", "Day12.txt"), "r") as f:
        lines = f.readlines()
        curr_shape = None
        shape_lines = 0
        count = 0
        for line in lines:
            count+=1
            line = line.strip()
            if not line:
                continue
            if ":" in line and line[1] == ":":
                curr_shape = int(line[0])
                shape_dict[curr_shape] = 0
                shape_lines = 3
            elif shape_lines > 0 and curr_shape is not None:
                shape_dict[curr_shape] += line.count("#")
                shape_lines -= 1
            elif ":" in line:
                key_, values = line.split(":")
                area_dict[f"{key_.strip()}_{count}"] = values.split(" ")[1:]
    return shape_dict, area_dict

def part1():
    shape_dict, area_dict = load_data()
    fitting_regions = 0
    for key_ in area_dict.keys():
        area = key_.split("_")
        area = area[0].split("x")
        fitting_area = int(area[0]) * int(area[1])
        actual_area = 0
        for i, count in enumerate(area_dict[key_]):
            actual_area += shape_dict[i] * int(count)
        if actual_area <= fitting_area:
            fitting_regions +=1
    return fitting_regions



if __name__ == "__main__":
    print("AOC 2025 - Day 12")
    print("Part 1:", part1())
    print("Part 2:", "Merry Christmas!")