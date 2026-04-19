import csv
import glob
import os
import heapq

def get_matrix(file_path):
    mat = []
    with open(file_path) as f:
        for row in csv.reader(f):
            # i am extracting the numbers from csv
            mat.append([float(x) for x in row if x.strip()])
    return mat

def length(matrix, path):
    """Calculates the exact cost of the given path."""
    cost = 0
    for i in range(len(path) - 1):
        cost += matrix[path[i]][path[i+1]]
    return cost

def bound(matrix, path):
    """
    calculates the lower bound for the remaining path.
    """
    n = len(matrix)
    cost = length(matrix, path)
    
    last_node = path[-1]
    unvisited = set(range(n)) - set(path)
    
    # if all nodes are visited, the bound is just the cost + trip back to start
    if not unvisited:
        return cost + matrix[last_node][path[0]]
        
    # i am finding the minimum edge from the current location to any other unvisited node
    min_from_current = float('inf')
    for v in unvisited:
        if matrix[last_node][v] < min_from_current:
            min_from_current = matrix[last_node][v]
            
    cost += min_from_current
    
    # finding the minimum edge from each unvisited node to another unvisited node or the start node
    for u in unvisited:
        min_from_u = float('inf')
        # i am checking the edges to other unvisited nodes and the start node (path[0])
        for v in unvisited.union({path[0]}):
            if u != v and matrix[u][v] < min_from_u:
                min_from_u = matrix[u][v]
        cost += min_from_u
        
    return cost

def solve_bb(matrix, start=0):
    n = len(matrix)
    
    # i am using a priority queue to store tuples of (bound_value, current_path)
    initial_path = [start]
    pq = [(bound(matrix, initial_path), initial_path)]
    
    best_cost = float('inf')
    best_tour = []
    
    while pq:
        # pop the path with the lowest bound
        current_bound, path = heapq.heappop(pq)
        
        # i am pruning here
        # if the best possible outcome of this path is worse than our best tour then skipping it.
        if current_bound >= best_cost:
            continue
            
        # if we have visited all the nodes, complete the tour and check the total cost
        if len(path) == n:
            total_cost = length(matrix, path) + matrix[path[-1]][start]
            if total_cost < best_cost:
                best_cost = total_cost
                best_tour = path + [start]
            continue
            
        # i am exploring all possible next unvisited nodes
        unvisited = set(range(n)) - set(path)
        for next_node in unvisited:
            new_path = path + [next_node]
            new_bound = bound(matrix, new_path)
            
            # i am adding to queue if it's less than current best cost
            if new_bound < best_cost:
                heapq.heappush(pq, (new_bound, new_path))
                
    return best_tour, best_cost

# i  am looping through all the csv files in the data folder
files = glob.glob("./data/*n.csv")
files.sort(key=lambda x: int(os.path.basename(x).split('n')[0]))

print("For Branch and Bound: ")
print("File   | Tour | Total Weight")
print("-" * 50)

for f in files:
    mat = get_matrix(f)
    tour, w = solve_bb(mat, 0)
    
    path = ",".join(str(node) for node in tour)
    fname = os.path.basename(f)
    
    print(f"{fname} | {path} | {w}")