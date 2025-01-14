import random

def random_graph(n, max_edges):
    edges = set()
    while len(edges) < max_edges:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:
            edge = (min(u, v), max(u, v))
            edges.add(edge)
    
    edges_list = list(edges)
    
    filename = f"./in/random_graph_{n}.in"
    with open(filename, "w") as f:
        f.write(f"{n} {len(edges_list)}\n")
        for edge in edges_list:
            f.write(f"{edge[0]} {edge[1]}\n")

def random_graph_generator(min_n, max_n, density):
    for n in range(min_n, max_n + 1):
        max_possible_edges = n * (n - 1) // 2
        max_edges = int(max_possible_edges * density)
        random_graph(n, max_edges)
        if density > 0.3:
            density -= 0.1
