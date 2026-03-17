import time

class GraphMatrix:
    """
    Adjacency matrix
    """
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.matrix = [None] * num_nodes
        for i in range(num_nodes):
            self.matrix[i] = [float('inf')] * num_nodes
            self.matrix[i][i] = 0.0
            
    def add_edge(self, source, destination, distance):
        self.matrix[source][destination] = float(distance)
    
def load_graph_matrix(filepath):
    max_node_id = 0
    edge_count = 0
    # here we are finding the max_node_id and counting edges to pre-allocate an array
    with open(filepath, 'r') as file:
        header = True
        for line in file:
            if header:
                header=False
                continue
            parts = line.strip().split(',')
            if len(parts)>=3:
                source = int(parts[0])
                dest = int(parts[1])
                if source> max_node_id:
                    max_node_id = source
                if dest>max_node_id:
                    max_node_id=dest
                edge_count+=1
    num_nodes = max_node_id+1
    
    edges_src = [0]*edge_count
    edges_dst = [0]*edge_count
    edges_wt = [0.0]*edge_count
    # here we are storing the edges
    with open(filepath, 'r') as file:
        header=True
        idx=0
        for line in file:
            if header:
                header=False
                continue
            parts = line.strip().split(',')
            if len(parts)>=3:
                edges_src[idx] = int(parts[0])
                edges_dst[idx] = int(parts[1])
                edges_wt[idx] = float(parts[2])
                idx+=1
        graph_matrix = GraphMatrix(num_nodes)
        
        for i in range(edge_count):
            graph_matrix.add_edge(edges_src[i], edges_dst[i], edges_wt[i])
        return graph_matrix, num_nodes, edge_count

def dijkstra_matrix(graph, source):
    num_nodes = graph.num_nodes
    dist = [float('inf')]*num_nodes
    prev = [None]* num_nodes
    visited=[False] *num_nodes
    dist[source]=0.0
    # finding the unviisted node with the minimum distance
    for k in range(num_nodes):
        min_dist = float('inf')
        u=-1
        for i in range(num_nodes):
            if not visited[i] and dist[i]< min_dist:
                min_dist = dist[i]
                u=i
        
        if u==-1:
            break
        # updating the distance of adjacent vertices
        visited[u]=True
        for v in range(num_nodes):
            weight = graph.matrix[u][v]
            if weight !=float('inf') and not visited[v]:
                updated_dist = dist[u]+ weight
                if updated_dist<dist[v]:
                    dist[v] = updated_dist
                    prev[v] = u
    return dist, prev

def get_path(dist, prev, source, dest, num_nodes):
    """
    reconstructing the path from dest to source
    """
    if dist[dest]==float('inf'):
        return None, float('inf')
    
    path_arr = [None]* num_nodes
    current = dest
    path_idx = num_nodes-1
    # i am tracing back dest to source
    while current is not None:
        path_arr[path_idx] = current
        current = prev[current]
        path_idx -=1
    
    valid_path_len = (num_nodes-1) - path_idx
    final_path = [None]* valid_path_len
    
    for i in range(valid_path_len):
        final_path[i]= path_arr[path_idx+1+i]
    
    return final_path, dist[dest]

if __name__ =="__main__":
    runtimes = [0.0] * 15
    memories = [0.0] * 15  # kilobytes
    
    for i in range(1, 16):
        filename = f"Project2_Input_File/Project2_Input_File{i}.csv"
        print(f"\nProcessing {filename}...")
        
        start_time = time.time()
        
        #i am constructing the graph and counting the number of nodes and edges to calculate memory usage later
        graph, nodes, edges = load_graph_matrix(filepath=filename)
        
        # i am computing all-pairs shortest paths by running dijkstra for each source node
        for src in range(nodes):
            dijkstra_matrix(graph, src)
            
        end_time = time.time()
        elapsed = end_time - start_time
        runtimes[i-1] = elapsed
        
        # calculating memory usage: adjacency matrix + dist array + prev array + visited array
        memory_bytes = (nodes * nodes * 8) + (nodes * 8) + (nodes * 8) + nodes
        memory_kb = memory_bytes / 1024
        memories[i-1] = memory_kb
        
        print(f"  1. Time Performance: {elapsed:.4f} seconds")
        print(f"  2. Memory Usage: {memory_kb:.2f} KB")
        
        if i == 4:
            print("\n" + "="*40 + "\nTEST CASES for FILE 4\n" + "="*40)
            sources = [192, 138, 465]
            destinations = [163, 66, 22]
            for test_source, test_dest in zip(sources, destinations):
                distances, predecessors = dijkstra_matrix(graph, test_source)
                path, total_dist = get_path(distances, predecessors, test_source, test_dest, nodes)
                print(f"Route: {test_source} -> {test_dest}\nDistance: {total_dist} feet\nPath: {path}\n")
            print("="*40 + "\n")

    # i am saving to csv for further plotting
    csv_filename = "dijkstra_2d_array.csv"
    with open(csv_filename, 'w') as f:
        f.write("file_id,time,memory\n")
        for i in range(15):
            f.write(f"{i+1},{runtimes[i]:.6f},{memories[i]:.2f}\n")
            
    print(f"\n Final Report Data saved to {csv_filename}")