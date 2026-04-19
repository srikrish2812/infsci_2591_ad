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

def solve_dp(matrix, start=0):
    n = len(matrix)
    memo = {}
    
    # this is a helper function to run the recursion
    # 'curr' is our current node,
    # 'mask' tells us which nodes are unvisited
    def tsp(curr, mask):
        # base case:mask is 0, means no unvisited nodes are there
        if mask == 0:
            # we simply return the cost to go back to the start
            return matrix[curr][start], [start]
            
        # i am checking if we've already done this exact calculation
        state = (curr, mask)
        if state in memo:
            return memo[state]
            
        min_cost = float('inf')
        best_path = []
        
        # i am trying every possible next node that is still unvisited
        for j in range(n):
            # bitwise check: is the j-th node still unvisited in our mask?
            if (mask & (1 << j)):
                
                # i  am creating a new mask that marks 'j' as visited
                new_mask = mask ^ (1 << j)
                
                # finding the cost for going from curr to j, plus the cost of the rest of the tour starting from j
                cost_of_rest, path_of_rest = tsp(j, new_mask)
                
                total_cost = matrix[curr][j] + cost_of_rest
                
                # updating min cost and best path
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = [j] + path_of_rest
                    
        memo[state] = (min_cost, best_path)
        return memo[state]

    # set up the initial bitmask: all 1s for all unvisited nodes
    initial_mask = (1 << n) - 1
    # for the start i  am setting its bit to 0 since it's already visited
    initial_mask = initial_mask ^ (1 << start)
    min_cost, best_path = tsp(start, initial_mask)
    
    # building the final list of nodes
    tour = [start] + best_path
    return tour, min_cost

# i am looping through all the csv files in the data folder
files = glob.glob("./data/*n.csv")
files.sort(key=lambda x: int(os.path.basename(x).split('n')[0]))

print("For Dynamic Programming: ")
print("File   | Tour | Total Weight")
print("-" * 50)

for f in files:
    mat = get_matrix(f)
    tour, w = solve_dp(mat, start=0)
    path = ",".join(str(node) for node in tour)
    fname = os.path.basename(f)
    
    print(f"{fname} | {path} | {w}")