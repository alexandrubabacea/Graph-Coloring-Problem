# inspired by: https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/

def add_neighbors(node, neighbors):
    for i in neighbors:
        node.append(i)
        
def read_graph_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        nodes_number, edges_number = map(int, lines[0].split())
        graph = [[] for _ in range(nodes_number)]

        for line in lines[1:]:
            u, v = map(int, line.split())
            graph[u].append(v)
            graph[v].append(u)

    return graph
    
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
    graph = read_graph_from_file("good_order_chrown_graph.in")
    
    print(f"Best order case of chrown graph with {len(graph)} nodes:")
    display_graph(graph)
    coloring = greedy_coloring(graph)
    
    for i in range(len(graph)):
        print(f"{i+1} has color: {coloring[i]}")
    colors_nr = len(set(coloring)) 
    print(f"Used {colors_nr} colors")
        
    #####################################################################
    print(f"\nWorst order case of chrown graph with {len(graph)} nodes:")
    
    graph = read_graph_from_file("bad_order_chrown_graph.in")
    
    display_graph(graph)
    coloring = greedy_coloring(graph)
    
    for i in range(len(graph)):
        print(f"{i+1} has color: {coloring[i]}")
    colors_nr = len(set(coloring)) 
    print(f"Used {colors_nr} colors")

if __name__ == "__main__":
    main()