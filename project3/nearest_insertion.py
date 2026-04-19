import csv
import glob
import os

def get_matrix(file_path):
    mat = []
    with open(file_path) as f:
        for row in csv.reader(f):
            # i am extracting the numbers from csv
            mat.append([float(x) for x in row if x.strip()])
    return mat

def solve_ni(matrix):
    n = len(matrix)
    
    # i am finding the absolute shortest link in the whole graph to start
    min_edge = float("inf")
    u, v = -1, -1
    
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] < min_edge:
                min_edge = matrix[i][j]
                u = i
                v = j
                
    # starting the tour as a mini-cycle between the two closest nodes
    # i am starting with u, then v, and then back to u to make it a cycle   
    tour = [u, v, u]
    visited = {u, v}
    unvisited = set(range(n)) - visited
    
    # i am adding nodes until we've visited them all
    while unvisited:
        
        # finding the unvisited node closest to any node currently in the tour
        best_k = -1
        min_dist_to_tour = float("inf")
        
        for node in unvisited:
            # skipping last node since it is same as first node in tour
            for t_node in tour[:-1]:
                if matrix[node][t_node] < min_dist_to_tour:
                    min_dist_to_tour = matrix[node][t_node]
                    best_k = node
                    
        # finding the best place to insert best_k into the tour
        best_idx = -1
        min_insert_cost = float("inf")
        
        for i in range(len(tour) - 1):
            curr_node = tour[i]
            next_node = tour[i+1]
            
            # dist from best_k to curr_node + dist from best_k to next_node - dist from curr_node to next_node
            cost = matrix[curr_node][best_k] + matrix[best_k][next_node] - matrix[curr_node][next_node]
            
            if cost < min_insert_cost:
                min_insert_cost = cost
                best_idx = i
                
        # inserting it right after best_idx in the tour 
        tour.insert(best_idx + 1, best_k)
        unvisited.remove(best_k)

    # summing up the total weight of the tour
    weight = sum(matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    

    zero_idx = tour.index(0)
    # slice the list to start at 0, and append 0 at the end
    tour = tour[zero_idx:-1] + tour[:zero_idx] + [0]
    
    return tour, weight

# i am looping through all the csv files in the data folder
files = glob.glob("./data/*n.csv")
files.sort(key=lambda x: int(os.path.basename(x).split('n')[0]))

print("For Nearest Insertion: ")
print("File   | Tour | Total Weight")
print("-" * 50)

for f in files:
    mat = get_matrix(f)
    tour, w = solve_ni(mat)
    path = ",".join(str(node) for node in tour)
    fname = os.path.basename(f)
    
    print(f"{fname} | {path} | {w}")