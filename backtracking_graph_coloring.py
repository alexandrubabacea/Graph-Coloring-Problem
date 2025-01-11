# inspired by: https://www.geeksforgeeks.org/graph-coloring-applications/
solution = False

def add_neighbors(node, neighbors):
    for i in neighbors:
        node.append(i)
    
def display_graph(graph):
    for i in range(len(graph)):
        print(f"{i+1}: ", end="")
        for neighbor in graph[i]:
            print(f"{neighbor+1} ", end="")
        print()

def is_valid(graph, coloring, current_vertex, color):
    
    for neighbor in graph[current_vertex]:
        if coloring[neighbor] == color:
            return False
        
    return True
        

def backtrack_coloring(graph, k, coloring, current_vertex):
    if current_vertex == len(graph):
        global solution
        solution = True
        for i in range(len(graph)):
            print(f"{i+1} has color {coloring[i]}")
        print("--------------")
        return
    
    for color in range(k):
        if is_valid(graph, coloring, current_vertex, color):
            coloring[current_vertex] = color
            
            backtrack_coloring(graph, k, coloring, current_vertex + 1)
        
            coloring[current_vertex] = -1
            
    

def main():
    nodes_number = 8
    k = 1
    
    graph = [[] for _ in range(nodes_number)]
    
    add_neighbors(graph[0], [3, 5, 7])
    add_neighbors(graph[1], [2, 4, 6])
    add_neighbors(graph[2], [1, 5, 7])
    add_neighbors(graph[3], [0, 4, 6])
    add_neighbors(graph[4], [1, 3, 7])
    add_neighbors(graph[5], [0, 2, 6])
    add_neighbors(graph[6], [1, 3, 5])
    add_neighbors(graph[7], [0, 2, 4])
    
    display_graph(graph)
    
    coloring = [-1] * len(graph)
    backtrack_coloring(graph, k, coloring, 0)
    
    if not solution:
        print(f"Doesn't exist a coloring with {k} color(s)")

if __name__ == "__main__":
    main()