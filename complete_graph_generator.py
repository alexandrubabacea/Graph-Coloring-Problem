def complete_graph(n):
    edges = []
    for i in range(n):
        for j in range(n):
            if j > i:
                edges.append([i, j])
    
    filename = f"./in/complete_graph_{n}.in"    
    with open(filename, "w") as f:
        f.write(f"{n} {n * (n-1) // 2}\n")
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")
            
def complete_graph_generator(min_n, max_n):
    for n in range(min_n, max_n + 1):
        complete_graph(n)
    