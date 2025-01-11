# inspired by: https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/

def add_neighbors(node, neighbors):
    for i in neighbors:
        node.append(i)
    
def display_graph(graph):
    for i in range(len(graph)):
        print(f"{i+1}: ", end="")
        for neighbor in graph[i]:
            print(f"{neighbor+1} ", end="")
        print()
        
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
    
    coloring = greedy_coloring(graph)
    
    for i in range(len(graph)):
        print(f"{i+1} has color: {coloring[i]}")
        
    display_graph(graph2)
    
    coloring2 = greedy_coloring(graph2)
    
    for i in range(len(graph2)):
        print(f"{i+1} has color: {coloring2[i]}")

if __name__ == "__main__":
    main()