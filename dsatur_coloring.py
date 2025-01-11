def add_neighbors(node, neighbors):
    for i in neighbors:
        node.append(i)
    
def display_graph(graph):
    for i in range(len(graph)):
        print(f"{i+1}: ", end="")
        for neighbor in graph[i]:
            print(f"{neighbor+1} ", end="")
        print()

def dsatur_coloring(graph):
    num_vertices = len(graph)

    result = [-1] * num_vertices
    saturation = [0] * num_vertices
    degrees = [len(neighbors) for neighbors in graph]
    
    for _ in range(num_vertices):
        # get the uncolored vertex with the maximum degree of the vertices with the maximum saturation
        not_visited_saturation = [saturation[i] for i in range(num_vertices) if result[i] == -1]
        max_saturation = max(not_visited_saturation)
        candidates = [i for i in range(num_vertices) if result[i] == -1 and saturation[i] == max_saturation]
        vertex = max(candidates, key=lambda x: degrees[x])
        
        # assign the smallest available color
        neighbor_colors = {result[neighbor] for neighbor in graph[vertex] if result[neighbor] != -1}
        color = 0
        while color in neighbor_colors:
            color += 1
        result[vertex] = color
        
        # update saturation of neighbors
        for neighbor in graph[vertex]:
            if result[neighbor] == -1:
                saturation[neighbor] += 1
    
    return result

def main():
    nodes_number = 8
    graph = [[] for _ in range(nodes_number)]
    
    add_neighbors(graph[0], [5, 6, 7])
    add_neighbors(graph[1], [4, 6, 7])
    add_neighbors(graph[2], [4, 5, 7])
    add_neighbors(graph[3], [4, 5, 6])
    add_neighbors(graph[4], [1, 2, 3])
    add_neighbors(graph[5], [0, 2, 3])
    add_neighbors(graph[6], [0, 1, 3])
    add_neighbors(graph[7], [0, 1, 2])
    
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
    
    coloring = dsatur_coloring(graph)
    
    for i in range(len(graph)):
        print(f"{i+1} has color: {coloring[i]}")
        
    display_graph(graph2)
    
    coloring2 = dsatur_coloring(graph2)
    
    for i in range(len(graph2)):
        print(f"{i+1} has color: {coloring2[i]}")

if __name__ == "__main__":
    main()