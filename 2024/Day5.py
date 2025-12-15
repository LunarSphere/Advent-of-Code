#Alogorthim Learned:
# DFS: https://www.datacamp.com/tutorial/depth-first-search-in-python
# Topological Sort
def load_data():
    rules = []
    updates = []
    read_rules = True ## a bool to determine if we are reading rules or updates
    # alternatively could have implemented this by finding a way to figure out which line
    # I was last pointing to. 
    with open("input/day5.txt") as file:
        for line in file.readlines(): 
            line = line.strip() #strip the line
            if line.strip() == "": read_rules = False; continue #if line is empty stop reading rules and skip next if statement
            if read_rules: 
                vals = line.split("|")
                rules.append((int(vals[0]), int(vals[1])))
            if not read_rules:
                updates.append([int(s) for s in line.split(",")])
    file.close()
    return rules, updates

def valid_update(rules, update) -> bool:
    for i, num in enumerate(update):
        #sublist of relevant rules
        sub_rules = [rule for rule in rules if num == rule[0] and rule[1] in update] #grab sublist of tuples where tup[0] == current number in update list
        # also ensures corresponding rule is in 
        for j in sub_rules:
            if update.index(num) > update.index(j[1]): return False # if index of current num is larger than its rule pair it means the number is ahead of it which breaks the rule


    return True

def dfs(node, rules, stack,visited=None):
    #node: index of node in update
    # rules:  Directed acyclic graph
    # stack: stack represent order of values
    # visited: list of visited nodes represented as true or false
    if visited is None:
        visited = set()
    visited.add(node)
    if node in rules:
        for c in rules[node]:
            if c not in visited:
                dfs(c, rules, stack, visited)
    stack.insert(0,node)
    return stack

def invalid_update(rules, update) -> list[int]:
    # fix update by running a topological sort | bassically a DFS on a DAG results in an ordered list
    # Tidbit: Topological sort only works on DAG because its acyclic if done on a cyclic graph there would be a cyclic dependency
    # the rules are perfect for a DAG 
    sub_rules = {}
    for a, b in rules:
        if a in update and b in update:
            if a not in sub_rules:
                sub_rules[a] = []
            sub_rules[a].append(b)
    
    # builds an adjacency list for a graph with only relevant rules (Directed Acyclic graph)
    #update its a hell of a lot easier to do dfs with a dictionary of subrules
    stack = []   
    visited = set()
    for node in update:
        if node not in visited: # if nodes hasn't been visited do a depth first search
            stack = dfs(node, sub_rules, stack, visited)
    return stack[::-1]


def solve() -> int:
    # given list of rules about ordering of pages of updates determine correct order. 
    # add up middle value of correctly ordered updates
    valid_middle_val_sum = 0
    fixed_middle_val_sum = 0
    rules, updates = load_data()
    for update in updates:
        if valid_update(rules, update): 
            valid_middle_val_sum += update[len(update)//2]
        else:
            #implement part 2
            # since we are organizing a set of rules where one element must appear before another
            # i can treat our rules as a directed acyclic graph
            # a topological sort can be done on this graph to put the elements in correct order. 
            fixed_update = invalid_update(rules, update)
            fixed_middle_val_sum += fixed_update[len(fixed_update)//2]
    return valid_middle_val_sum, fixed_middle_val_sum

def main():
    ##5732, 4716
    print(solve())

    return 0; 
if __name__ == "__main__":
    main()
    print("Day 5: Completed")