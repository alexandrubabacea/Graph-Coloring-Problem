# inspired by: https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
        
def greedy_coloring(graph):
    # -1 means uncolored
    coloring = [-1] * len(graph) 
    
    # array for available colors for a specific node
    available_colors = [True] * len(graph)
    
    for i in range(len(graph)):
        
        # go through the node's neighbors to see their color
        for neighbor_nr in graph[i]:
            # get neighbor color
            color = coloring[neighbor_nr]
            
            # if neighbor is colored, mark it's color as unusable
            if color != -1:
                available_colors[color] = False
                
        # color the node with the first available color
        for j in range(len(available_colors)):
            if available_colors[j]:
                coloring[i] = j
                break
            
        # reset the available_colors array
        for j in range(len(available_colors)):
            available_colors[j] = True
            
    return coloring