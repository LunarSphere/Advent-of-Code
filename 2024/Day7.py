# based on this tutorial 
# https://youtu.be/Np6ti3t36XA?si=_SP1B7OC2JVWQN9O
def load_data():
    data_dict = {}
    with open("input/day7.txt", "r") as file:
        for line in file.readlines():
            strip_line = line.replace(":", "").strip().split(" ") #get rid of colon, remove \n make it a list
            data_dict[int(strip_line[0])] = [int(i) for i in strip_line[1::]]
    file.close()
    return data_dict


def check(expected, vals,part2 = False):
    if len(vals) == 1:
        return expected == vals[0]
    val = vals.pop()
    if expected%val == 0:
        if check(expected//val, vals[:], part2=part2):
            return True
    if expected - val >= 0:
        if check(expected-val, vals[:], part2=part2):
            return True
    expected_s = str(expected)
    val_s = str(val)
    if not part2:
        return False
    if expected_s.endswith(val_s) and len(expected_s) > len(val_s):
        new_expected = int(expected_s[:-len(val_s)])
        if check(new_expected, vals[:], True):
            return True
    return False    
        

def solve():
    #for each entry check it if could be true
    # return sum of potentially true
    calibration_total = 0
    calibration_total_2 = 0
    data_dict = load_data()
    for expected, vals in data_dict.items():
        if check(expected, vals[:]):
            calibration_total += expected
        if check(expected, vals[:], True):
            calibration_total_2 += expected
    return calibration_total, calibration_total_2



def main():
    print(solve())
    return

if __name__ == "__main__":
    main()