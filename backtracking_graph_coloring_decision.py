# inspired by: https://www.geeksforgeeks.org/graph-coloring-applications/

def is_valid(graph, coloring, current_vertex, color):
    
    for neighbor in graph[current_vertex]:
        if coloring[neighbor] == color:
            return False
        
    return True
        

def backtrack_coloring(graph, k, coloring, current_vertex):
    if current_vertex == len(graph):
        return True, coloring
    
    for color in range(k):
        if is_valid(graph, coloring, current_vertex, color):
            coloring[current_vertex] = color
            
            solution, coloring = backtrack_coloring(graph, k, coloring, current_vertex + 1)
            if solution:
                return True, coloring
        
            coloring[current_vertex] = -1
            
    return False, coloring