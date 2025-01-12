import greedy_graph_coloring as greedy
import backtracking_graph_coloring_optimal as backtr
import dsatur_coloring as dsatur
import crown_graph_generator as crown_gen

import networkx as nx
import matplotlib.pyplot as plt
import time

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
        print(f"{i}: ", end="")
        for neighbor in graph[i]:
            print(f"{neighbor} ", end="")
        print()
        
def plot_graph(G, coloring, filename):
    nodes = G.nodes()
    color_map = {i: plt.cm.rainbow(i / (max(coloring) + 1)) for i in range(max(coloring) + 1)}
    node_colors = [color_map[coloring[i]] for i in nodes]
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=16)
    plt.savefig(filename)
    
        
############################# good order crown graph #############################
def good_order_crown_graph():
    crown_gen.generate_good_order_cg()
    graph = read_graph_from_file("good_order_crown_graph.in")
    
    print(f"Best order case of crown graph with {len(graph)} nodes:")
    # display_graph(graph)
    
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    start_time = time.time()
    coloring_backtracking = backtr.backtr_optimal(graph)
    end_time = time.time()
    plot_graph(G, coloring_backtracking, "./images/good_order_crown_graph_backtracking.png")
    colors_nr = len(set(coloring_backtracking))
    print(f"Backtracking used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    start_time = time.time()
    coloring_greedy = greedy.greedy_coloring(graph)
    end_time = time.time()
    plot_graph(G, coloring_greedy, "./images/good_order_crown_graph_greedy.png")
    colors_nr = len(set(coloring_greedy)) 
    print(f"Greedy used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    start_time = time.time()
    coloring_dsatur = dsatur.dsatur_coloring(graph)
    end_time = time.time()
    plot_graph(G, coloring_dsatur, "./images/good_order_crown_graph_dsatur.png")
    colors_nr = len(set(coloring_dsatur)) 
    print(f"Dsatur used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    print()
    
############################# bad order crown graph #############################
def bad_order_crown_graph():
    crown_gen.generate_bad_order_cg()
    graph = read_graph_from_file("bad_order_crown_graph.in")
    
    print(f"Worst order case of crown graph with {len(graph)} nodes:")
    # display_graph(graph)
    
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
            
    start_time = time.time()
    coloring_backtracking = backtr.backtr_optimal(graph)
    end_time = time.time()
    plot_graph(G, coloring_backtracking, "./images/bad_order_crown_graph_backtracking.png")
    colors_nr = len(set(coloring_backtracking)) 
    print(f"Backtracking used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    start_time = time.time()
    coloring_greedy = greedy.greedy_coloring(graph)
    end_time = time.time()
    plot_graph(G, coloring_greedy, "./images/bad_order_crown_graph_greedy.png")
    colors_nr = len(set(coloring_greedy)) 
    print(f"Greedy used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    start_time = time.time()
    coloring_dsatur = dsatur.dsatur_coloring(graph)
    end_time = time.time()
    plot_graph(G, coloring_dsatur, "./images/bad_order_crown_graph_dsatur.png")
    colors_nr = len(set(coloring_dsatur)) 
    print(f"Dsatur used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    print()
    
############################# good order chordal graph #############################
def good_order_chordal_graph():
    graph = read_graph_from_file("good_order_chordal_graph.in")
    
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    if nx.is_chordal(G):
        print(f"Well ordered nodes in chordal graph with {len(graph)} nodes:")
        display_graph(graph)
        
        start_time = time.time()
        coloring_backtracking = backtr.backtr_optimal(graph)
        end_time = time.time()
        plot_graph(G, coloring_backtracking, "./images/good_order_chordal_graph_backtracking.png")
        colors_nr = len(set(coloring_backtracking)) 
        print(f"Backtracking used {colors_nr} colors.")
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        
        start_time = time.time()
        coloring_greedy = greedy.greedy_coloring(graph)
        end_time = time.time()
        plot_graph(G, coloring_greedy, "./images/good_order_chordal_graph_greedy.png")
        colors_nr = len(set(coloring_greedy)) 
        print(f"Greedy used {colors_nr} colors.")
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        
        start_time = time.time()
        coloring_dsatur = dsatur.dsatur_coloring(graph)
        end_time = time.time()
        plot_graph(G, coloring_dsatur, "./images/good_order_chordal_graph_dsatur.png")
        colors_nr = len(set(coloring_dsatur)) 
        print(f"Dsatur used {colors_nr} colors.")
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
    else:
        print("Graph is not chordal")
        
    print()
        
############################# bad order chordal graph #############################
def bad_order_chordal_graph():
    graph = read_graph_from_file("bad_order_chordal_graph.in")
    
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    if nx.is_chordal(G):
        print(f"Bad ordered nodes in chordal graph with {len(graph)} nodes:")
        display_graph(graph)
        
        start_time = time.time()
        coloring_backtracking = backtr.backtr_optimal(graph)
        end_time = time.time()
        plot_graph(G, coloring_backtracking, "./images/bad_order_chordal_graph_backtracking.png")
        colors_nr = len(set(coloring_backtracking)) 
        print(f"Backtracking used {colors_nr} colors.")
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        
        start_time = time.time()
        coloring_greedy = greedy.greedy_coloring(graph)
        end_time = time.time()
        plot_graph(G, coloring_greedy, "./images/bad_order_chordal_graph_greedy.png")
        colors_nr = len(set(coloring_greedy)) 
        print(f"Greedy used {colors_nr} colors.")
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        
        start_time = time.time()
        coloring_dsatur = dsatur.dsatur_coloring(graph)
        end_time = time.time()
        plot_graph(G, coloring_dsatur, "./images/bad_order_chordal_graph_dsatur.png")
        colors_nr = len(set(coloring_dsatur)) 
        print(f"Dsatur used {colors_nr} colors.")
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
    else:
        print("Graph is not chordal") 
        
    print()
    
############################# backtracking graph #############################
def backtracking_graph():
    graph = read_graph_from_file("backtracking_graph.in")
    
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    print(f"Backtracking graph with {len(graph)} nodes:")
    display_graph(graph)
    
    start_time = time.time()
    coloring_backtracking = backtr.backtr_optimal(graph)
    end_time = time.time()
    plot_graph(G, coloring_backtracking, "./images/graph_backtracking.png")
    colors_nr = len(set(coloring_backtracking)) 
    print(f"Backtracking used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    start_time = time.time()
    coloring_greedy = greedy.greedy_coloring(graph)
    end_time = time.time()
    plot_graph(G, coloring_greedy, "./images/graph_greedy.png")
    colors_nr = len(set(coloring_greedy)) 
    print(f"Greedy used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
    
    start_time = time.time()
    coloring_dsatur = dsatur.dsatur_coloring(graph)
    end_time = time.time()
    plot_graph(G, coloring_dsatur, "./images/graph_dsatur.png")
    colors_nr = len(set(coloring_dsatur)) 
    print(f"Dsatur used {colors_nr} colors.")
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
        
    print()
    
def main():
    good_order_crown_graph()
    bad_order_crown_graph()
    good_order_chordal_graph()
    bad_order_chordal_graph()
    backtracking_graph()

if __name__ == "__main__":
    main()