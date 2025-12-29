from functools import lru_cache
import os

### this one was laugably easy

def load_data():
    adjacency_list = {}
    with open(os.path.join("inputs", "Day11.txt")) as f:
        for line in f:
            line = line.strip()
            adjacency_list[line.split(":")[0]] = line.split(":")[1].strip().split(" ")
    return adjacency_list


def part1():
    data = load_data()
    def bfs(start_node, end_node):
        open_ = [start_node] #FIFO QUEUE
        paths = 0
        while open_:
            node = open_.pop(0)
            for child in data[node]:
                if child == end_node:
                    paths +=1
                    continue
                else:
                    open_.append(child)
        return paths
    return bfs('you', 'out') 


def part2():
    data = load_data()

    @lru_cache(maxsize=None)
    def dfs(node, visit_dac=False, visit_fft=False):
        total_paths = 0
        for child in data[node]:
            if not visit_dac:
                new_visit_dac = (child == "dac")
            else:
                new_visit_dac = visit_dac
            if not visit_fft:
                new_visit_fft = (child == "fft")
            else:
                new_visit_fft = visit_fft
            if child == "out":
                if visit_dac and visit_fft:
                    total_paths +=1
                continue
            total_paths += dfs(child, new_visit_dac, new_visit_fft)
        return total_paths

            
            

    return dfs('svr') 

                





if __name__ == "__main__":
    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")