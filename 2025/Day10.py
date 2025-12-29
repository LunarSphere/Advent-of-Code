import os
import re
from pulp import LpMinimize, LpProblem, LpVariable, PULP_CBC_CMD, lpSum

# refrences: https://yordi.me/advent-of-code-2025-day-10/
# part 2
def load_data():
    with open(os.path.join("inputs", "Day10.txt")) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def data_helper(line):
    """input: string represnting a line of data 
        output: goal state, possible actions, what ever last list represents
        """
    pattern = re.compile(r"""
    \[.*?\] |
    \{.*?\} |
    \(\d+(?:,\d+)*\)
    """, re.VERBOSE)

    tokens = pattern.findall(line)
    goal_state = ""
    idk = []
    actions = []
    
    for t in tokens:
        if t.startswith('['):
            goal_state = list(t[1:-1])
            goal_state = [0 if i == "." else 1 for i in goal_state]
        if t.startswith('{'):
            idk = list(map(int, t[1:-1].split(',')))
        if t.startswith('('):
            actions.append(tuple(map(int, t[1:-1].split(','))))
    return goal_state, actions, idk

def bfs(goal_state, actions):
    start_state = [0 for i in goal_state]
    open_ = []
    open_.append((start_state, []))
    closed = []
    while open_:
        node, path = open_.pop(0)
        if node in closed:
            continue
        closed.append(node)
        for i, action in enumerate(actions):
            child = node.copy()
            # apply actionto create the child
            for flip in action:
                if child[flip] == 1:
                    child[flip] = 0
                elif child[flip] == 0:
                    child[flip] = 1
            # if child not in closded and not in open see if its to goal state else 
            if child not in closed and child not in open_:
                new_path = path + [i]
                if child == goal_state:
                    return new_path
                else:
                    open_.append((child, new_path))
    return [[]]

def part1():
    data = load_data()
    shortest_path_total = 0
    for line in data:
        goal_state, actions, joltages = data_helper(line)
        # print(f"Goal State: {goal_state}\n Actions: {actions}\n IDK: {idk}") sanity check
        shortest_path_total += len(bfs(goal_state, actions))
    return shortest_path_total

def linear_solve(buttons, joltages):
    problem = LpProblem("configure_joltages", LpMinimize)
    variables = [LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(len(buttons))]
    problem += lpSum(variables)
    for i in range(len(joltages)):
        problem += lpSum(buttons[j][i] * variables[j] for j in range(len(buttons))) == joltages[i]
    problem.solve(PULP_CBC_CMD(msg=False))

    total = 0
    for var in variables:
        val = var.value()
        if val is None:
            total += 0
        else:
            total += int(float(val))
    return total




def part2():
    data = load_data()
    min_presses = 0
    for line in data:
        goal_state, actions, joltages = data_helper(line)
        #convert actions to binary vectors
        buttons_bin = []
        for button in enumerate(actions):
            button_bin = [0 for i in range(len(goal_state))]
            for index in button[1]:
                button_bin[index] = 1
            buttons_bin.append(button_bin)
        min_presses += linear_solve(buttons_bin, joltages)
    return min_presses

def main():
    print("part 1:", part1())
    print("part 2:", part2())

if __name__ == "__main__":
    main()