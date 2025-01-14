##################### good order chrown graph #####################
def generate_good_order_cg(n):

    group1 = [i for i in range(n)]
    group2 = [i for i in range(n, 2*n)]

    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                edge = [group1[i], group2[j]]
                edges.append(edge)
            
    filename = f"./in/good_order_crown_graph_{2*n}.in"    
    with open(filename, "w") as f:
        f.write(f"{2 * n} {len(edges)}\n")
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")
            
##################### bad order chrown graph ######################
def generate_bad_order_cg(n):

    group1 = [i for i in range(2*n) if i % 2 == 0]
    group2 = [i for i in range(2*n) if i % 2 == 1]

    edges = []
    for i in range(n):
        for j in range(n):
            if i != j:
                edge = [group1[i], group2[j]]
                edges.append(edge)
                
    filename = f"./in/bad_order_crown_graph_{2*n}.in"
    with open(filename, "w") as f:
        f.write(f"{2 * n} {len(edges)}\n")
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")
            
def crown_generator(min_n, max_n):
    for n in range(min_n, max_n+1):
        generate_bad_order_cg(n)
        generate_good_order_cg(n)
