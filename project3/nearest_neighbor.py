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


def solve_nn(matrix, start=0):
    n = len(matrix)
    visited = {start}
    tour = [start]
    weight = 0.0
    curr = start

    # outer loop thorugh n-1 nodes since we start at one node   
    for _ in range(n - 1):
        next_node = -1
        min_dist = float("inf")

        for j in range(n):
            # i am checking for unvisited and closer nodes to the current node
            if j not in visited and matrix[curr][j] < min_dist:
                min_dist = matrix[curr][j]
                next_node = j

        tour.append(next_node)
        visited.add(next_node)
        weight += min_dist
        curr = next_node

    # add the distance back to the starting node to complete the tour
    weight += matrix[curr][start]
    tour.append(start)

    return tour, weight


# i am looping through all the csv files in the data folder
files = glob.glob("./data/*n.csv")
files.sort(key=lambda x: int(os.path.basename(x).split("n")[0]))
print("For Nearest Neighbor: ")
print("File   | Tour | Total Weight")
print("-" * 50)

for f in files:
    mat = get_matrix(f)
    tour, w = solve_nn(mat, 0)
    path = ",".join(str(node) for node in tour)
    fname = os.path.basename(f)

    print(f"{fname}   | {path} | {w}")
