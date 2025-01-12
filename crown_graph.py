while True:
    n = int(input("Enter the number of nodes for the crown graph: "))
    if n % 2 == 0:
        n //= 2
        break
    else:
        print("Please enter an even number.")

##################### good order chrown graph #####################
group1 = [i for i in range(n)]
group2 = [i for i in range(n, 2*n)]

edges = []
for i in range(n):
    for j in range(n):
        if i != j:
            edge = [group1[i], group2[j]]
            edges.append(edge)
            
with open("good_order_chrown_graph.in", "w") as f:
    f.write(f"{2 * n} {len(edges)}\n")
    for edge in edges:
        f.write(f"{edge[0]} {edge[1]}\n")

##################### bad order chrown graph ######################

group1 = [i for i in range(2*n) if i % 2 == 0]
group2 = [i for i in range(2*n) if i % 2 == 1]

edges = []
for i in range(n):
    for j in range(n):
        if i != j:
            edge = [group1[i], group2[j]]
            edges.append(edge)
            
with open("bad_order_chrown_graph.in", "w") as f:
    f.write(f"{2 * n} {len(edges)}\n")
    for edge in edges:
        f.write(f"{edge[0]} {edge[1]}\n")