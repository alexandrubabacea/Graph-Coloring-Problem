def dsatur_coloring(graph):
    num_vertices = len(graph)

    coloring = [-1] * num_vertices
    saturation = [0] * num_vertices
    degrees = [len(neighbors) for neighbors in graph]
    
    for _ in range(num_vertices):
        # get the uncolored vertex with the maximum degree of the vertices with the maximum saturation
        not_visited_saturation = [saturation[i] for i in range(num_vertices) if coloring[i] == -1]
        max_saturation = max(not_visited_saturation)
        candidates = [i for i in range(num_vertices) if coloring[i] == -1 and saturation[i] == max_saturation]
        vertex = max(candidates, key=lambda x: degrees[x])
        
        # assign the smallest available color
        neighbor_colors = {coloring[neighbor] for neighbor in graph[vertex] if coloring[neighbor] != -1}
        color = 0
        while color in neighbor_colors:
            color += 1
        coloring[vertex] = color
        
        # update saturation of neighbors
        for neighbor in graph[vertex]:
            if coloring[neighbor] == -1:
                saturation[neighbor] += 1
    
    return coloring