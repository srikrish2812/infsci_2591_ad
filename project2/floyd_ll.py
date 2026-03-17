import time

class Node:
    """
    This node represents a directed edge to a dest with a specific distance
    """
    def __init__(self, destination_id, distance):
        self.destination_id = destination_id
        self.distance = distance
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, destination_id,distance):
        new_node = Node(destination_id, distance)
        new_node.next = self.head
        self.head = new_node

class GraphLinkedList:
    """
    adjacency list representation using a static array using custom linked list
    """
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = [None]*num_nodes
        for i in range(num_nodes):
            self.adj_list[i] = LinkedList()
    
    def add_edge(self, source, destination, distance):
        self.adj_list[source].insert(destination,distance)

def load_graph_ll(filepath):
    max_node_id = 0
    edge_count =0
    # i am finding max_node_id and counting edges
    with open(filepath, 'r') as file:
        header=True
        for line in file:
            if header:
                header=False
                continue
            parts = line.strip().split(',')
            if len(parts)>=3:
                source = int(parts[0])
                dest = int(parts[1])
                if source>max_node_id:
                    max_node_id = source
                if dest>max_node_id:
                    max_node_id = dest
                edge_count+=1
    num_nodes = max_node_id+1
    edges_src = [0]*edge_count
    edges_dest = [0]* edge_count
    edges_wt = [0.0]* edge_count
    
    # i am storing edges
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
                edges_dest[idx] = int(parts[1])
                edges_wt[idx] = float(parts[2])
                idx+=1
        graph_ll = GraphLinkedList(num_nodes)
        
        for i in range(edge_count):
            graph_ll.add_edge(edges_src[i], edges_dest[i], edges_wt[i])
        return graph_ll, num_nodes, edge_count

def floyd_linkedlist(graph):
    """
    Floyd's algorithm using adjacency list (linked list)
    """
    num_nodes = graph.num_nodes
    dist = [None]*num_nodes
    next_node = [None]*num_nodes
    for i in range(num_nodes):
        dist[i] = [float('inf')]*num_nodes
        next_node[i] = [None]*num_nodes
        dist[i][i] = 0.0
        
        current_node = graph.adj_list[i].head
        while current_node is not None:
            j = current_node.destination_id
            weight = current_node.distance
            dist[i][j] = weight
            next_node[i][j] = j
            current_node = current_node.next
    
    for k in range(num_nodes):
        for i in range(num_nodes):
            # i am skipping if intermediate node k is not reachable from i
            if dist[i][k] == float('inf'):
                continue
            for j in range(num_nodes):
                if dist[k][j] == float('inf'):
                    continue
                updated_dist = dist[i][k] + dist[k][j]
                if updated_dist < dist[i][j]:
                    dist[i][j] = updated_dist
                    next_node[i][j] = next_node[i][k]
    
    return dist, next_node

def get_floyd_path(next_node_matrix, source, dest, num_nodes):
    if next_node_matrix[source][dest] is None:
        return []
    
    path_arr = [None]* num_nodes
    path_arr[0] = source
    idx =1
    curr = source
    while curr != dest:
        curr = next_node_matrix[curr][dest]
        path_arr[idx] = curr
        idx+=1
    
    final_path = [None]* idx
    for i in range(idx):
        final_path[i] = path_arr[i]
    
    return final_path

if __name__ == "__main__":
    runtimes = [0.0] * 15
    memories = [0.0] * 15
    
    for i in range(1, 16):
        filename = f"Project2_Input_File/Project2_Input_File{i}.csv"
        print(f"\nProcessing {filename}...")
            
        start_time = time.time()
        
        graph, nodes, edge_count = load_graph_ll(filepath=filename)
        distances, next_nodes = floyd_linkedlist(graph)
            
        end_time = time.time()
        elapsed = end_time - start_time
        runtimes[i-1] = elapsed
        
        # Memory: LL size + 2x Matrices (Dist, Next_Node)
        memory_bytes = (nodes * 8) + (edge_count * 24) + 2 * (nodes * nodes * 8) + 2 * (nodes * 8)
        memory_kb = memory_bytes / 1024
        memories[i-1] = memory_kb
        
        print(f"  1. Time Performance: {elapsed:.4f} seconds")
        print(f"  2. Memory Usage: {memory_kb:.2f} KB")
        
        if i == 4:
            print("\n" + "="*40 + "\nTEST CASES for FILE 4\n" + "="*40)
            sources = [192, 138, 465]
            destinations = [163, 66, 22]
            for test_source, test_dest in zip(sources, destinations):
                path = get_floyd_path(next_nodes, test_source, test_dest, nodes)
                total_dist = distances[test_source][test_dest]
                print(f"Route: {test_source} -> {test_dest}\nDistance: {total_dist} feet\nPath: {path}\n")
            print("="*40 + "\n")

    csv_filename = "floyd_ll.csv"
    with open(csv_filename, 'w') as f:
        f.write("file_id,time,memory\n")
        for i in range(15):
            if runtimes[i] > 0:
                f.write(f"{i+1},{runtimes[i]:.6f},{memories[i]:.2f}\n")
            
    print(f"\n--- Final Report Data saved to {csv_filename} ---")