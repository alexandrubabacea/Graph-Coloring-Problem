def add_neighbors(node, neighbors):
    for i in neighbors:
        node.append(i)
    
def display_graph(graph):
    for i in range(len(graph)):
        print(f"{i+1}: ", end="")
        for neighbor in graph[i]:
            print(f"{neighbor+1} ", end="")
        print()

def rlf_coloring(graph):
    num_vertices = len(graph)
    uncolored = set(range(num_vertices))  # Set of all uncolored vertices
    coloring = [-1] * num_vertices  # Array to store the color of each vertex
    current_color = 0  # Start with the first color
    
    while uncolored:
        # Find the vertex with the largest number of neighbors
        start_vertex = max(uncolored, key=lambda v: len(graph[v]))
        independent_set = {start_vertex}
        
        # build the independent set
        for vertex in uncolored - independent_set:
            # add vertex if it is not adjacent to any vertex in the independent set
            if all(neighbor not in independent_set for neighbor in graph[vertex]):
                independent_set.add(vertex)
        
        # assign the current color to all vertices in the independent set
        for vertex in independent_set:
            coloring[vertex] = current_color
            uncolored.remove(vertex)
            
        current_color += 1
    
    return coloring

def main():
    nodes_number = 8
    graph = [[] for _ in range(nodes_number)]
    
    add_neighbors(graph[0], [1, 2, 3, 4, 5, 6, 7])
    add_neighbors(graph[1], [0, 2, 7])
    add_neighbors(graph[2], [0, 1, 3])
    add_neighbors(graph[3], [0, 2, 4])
    add_neighbors(graph[4], [0, 3, 5])   
    add_neighbors(graph[5], [0, 4, 6])
    add_neighbors(graph[6], [0, 5, 7])
    add_neighbors(graph[7], [0, 1, 6])
    
    graph2 = [[] for _ in range(nodes_number)]
    
    add_neighbors(graph2[0], [3, 5, 7])
    add_neighbors(graph2[1], [2, 4, 6])
    add_neighbors(graph2[2], [1, 5, 7])
    add_neighbors(graph2[3], [0, 4, 6])
    add_neighbors(graph2[4], [1, 3, 7])
    add_neighbors(graph2[5], [0, 2, 6])
    add_neighbors(graph2[6], [1, 3, 5])
    add_neighbors(graph2[7], [0, 2, 4])
    
    display_graph(graph)
    
    coloring = rlf_coloring(graph)
    
    for i in range(len(graph)):
        print(f"{i+1} has color: {coloring[i]}")
        
    display_graph(graph2)
    
    coloring2 = rlf_coloring(graph2)
    
    for i in range(len(graph2)):
        print(f"{i+1} has color: {coloring2[i]}")

if __name__ == "__main__":
    main()