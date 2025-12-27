import os
from shapely.geometry import Polygon

def load_data():
    with open(os.path.join("inputs", "day9.txt"), "r") as file:
        data = [line.strip() for line in file]
        data = [list(map(int, line.split(","))) for line in data] #convert to integers
    return data



def part1():
    data = load_data()

    #create list of pairs of indices
    index_pairs = [(i,j) for i in range(len(data)) for j in range(i+1, len(data))]
    def calculate_area(pair):
        pair_coords = (data[pair[0]], data[pair[1]])
        return (abs(pair_coords[0][0] - pair_coords[1][0]) +1 ) *  (abs(pair_coords[0][1] - pair_coords[1][1]) +1)
    # sort index by pair that has the largest area
    max_pair = max(index_pairs, key = calculate_area) 
    # print(index_pairs)
    # return area of largest pair probably should just make this a function
    return  calculate_area(max_pair)




def part2():
    """ part two was not for the faint of heart
        read this guys article 
        https://yordi.me/advent-of-code-2025-day-9/
        
    """
    
    def poly_rec_area(x1, y1, x2, y2):
        """Create a rectangle polygon from two points"""
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        return Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)])
    largest = 0

    data = load_data()
    polygon = Polygon(data) # make polygon from points we will use this to see if rectangles fit within it
    #for every coordinate pair
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            rectangle = poly_rec_area(x1, y1, x2, y2)
            # see if they make a rectangele within the polygon
            if rectangle.within(polygon):
                area = (abs(x1 - x2) +1) * (abs(y1 - y2) +1)
                if area > largest:
                    largest = area
    return largest
    



def main():
    print("Part 1:", part1())
    print("Part 2:", part2())

if __name__ == "__main__":
    main()