import greedy_graph_coloring as greedy
import backtracking_graph_coloring_optimal as backtr
import dsatur_coloring as dsatur

import crown_graph_generator as crown_gen
import complete_graph_generator as complete_gen
import random_graph_generator as rand_gen

import networkx as nx
import matplotlib.pyplot as plt
import time

backtracking_colors = []
greedy_colors = []
dsatur_colors = []

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
    plt.close()

def plot_execution_time_vs_nodes(nodes_range, backtracking_times, greedy_times, dsatur_times, test):
    plt.figure(figsize=(10, 6))
    plt.plot(nodes_range, backtracking_times, label='Backtracking', marker='o', color='red')
    plt.plot(nodes_range, greedy_times, label='Greedy', marker='s', color='blue')
    plt.plot(nodes_range, dsatur_times, label='DSatur', marker='^', color='green')
    plt.xticks([int(i) for i in nodes_range])
    plt.yticks([round(i, 3) for i in plt.yticks()[0]])
    plt.xlabel("Numărul de noduri")
    plt.ylabel("Timp (milisecunde)")
    title = f"Timpul de execuție în funcție de numărul de noduri ({test})"
    plt.title(title)
    plt.legend()
    plt.grid(True)
    filename = f"./images/plot_execution_time_vs_nodes_{test}"
    plt.savefig(filename)
    plt.close()
    
def plot_colors_used_vs_nodes(nodes_range, backtracking_colors, greedy_colors, dsatur_colors, test):
    plt.figure(figsize=(10, 6))
    plt.plot(nodes_range, backtracking_colors, label='Backtracking', marker='o', color='red')
    plt.plot(nodes_range, greedy_colors, label='Greedy', marker='s', color='blue')
    plt.plot(nodes_range, dsatur_colors, label='DSatur', marker='^', color='green')
    plt.xticks([int(i) for i in nodes_range])
    plt.xlabel('Numărul de noduri')
    plt.ylabel('Numărul de culori')
    title = f"Numărul de culori utilizate în funcție de numărul de noduri ({test})"
    plt.title(title)
    plt.legend()
    plt.grid(True)
    filename = f"./images/plot_colors_used_vs_nodes_{test}"
    plt.savefig(filename)
    plt.close()
        
############################# good order crown graph #############################
def good_order_crown_graph(n, iter):
    filename = f"./in/good_order_crown_graph_{2*n}.in"
    graph = read_graph_from_file(filename)
    
    global backtracking_colors
    global greedy_colors
    global dsatur_colors
    
    if iter == 0:
        print(f"Well ordered crown graph with {len(graph)} nodes:")
        display_graph(graph)
        
        if 2*n <= 30:
            G = nx.Graph()
            for node, neighbors in enumerate(graph):
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)      
    
    start_time = time.time()
    coloring_backtracking = backtr.backtr_optimal(graph)
    end_time = time.time()
    backtracking_time = end_time - start_time
    
    if iter == 0:
        if 2*n <= 30:
            filename = f"./images/good_order_crown_graph_backtracking_{2*n}.png"
            plot_graph(G, coloring_backtracking, filename)
        colors_nr = len(set(coloring_backtracking))
        backtracking_colors.append(colors_nr)
        print(f"Backtracking used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_greedy = greedy.greedy_coloring(graph)
    end_time = time.time()
    greedy_time = end_time - start_time
    
    if iter == 0:
        if 2*n <= 30:
            filename = f"./images/good_order_crown_graph_greedy_{2*n}.png"
            plot_graph(G, coloring_greedy, filename)
        colors_nr = len(set(coloring_greedy))
        greedy_colors.append(colors_nr)
        print(f"Greedy used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_dsatur = dsatur.dsatur_coloring(graph)
    end_time = time.time()
    dsatur_time = end_time - start_time
    
    if iter == 0:
        if 2*n <= 30:
            filename = f"./images/good_order_crown_graph_dsatur_{2*n}.png"
            plot_graph(G, coloring_dsatur, filename)
        colors_nr = len(set(coloring_dsatur))
        dsatur_colors.append(colors_nr)
        print(f"Dsatur used {colors_nr} colors.")
    
    times = [backtracking_time, greedy_time, dsatur_time]
    return times
    
############################# bad order crown graph #############################
def bad_order_crown_graph(n, iter):
    filename = f"./in/bad_order_crown_graph_{2*n}.in"
    graph = read_graph_from_file(filename)
    
    if iter == 0:
        print(f"Bad ordered crown graph with {len(graph)} nodes:")
        display_graph(graph)
        
        if 2*n <= 30:
            G = nx.Graph()
            for node, neighbors in enumerate(graph):
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)
            
    start_time = time.time()
    coloring_backtracking = backtr.backtr_optimal(graph)
    end_time = time.time()
    backtracking_time = end_time - start_time
    
    if iter == 0:
        if 2*n <= 30:
            filename = f"./images/bad_order_crown_graph_backtracking_{2*n}.png"
            plot_graph(G, coloring_backtracking, filename)
        colors_nr = len(set(coloring_backtracking))
        backtracking_colors.append(colors_nr)
        print(f"Backtracking used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_greedy = greedy.greedy_coloring(graph)
    end_time = time.time()
    greedy_time = end_time - start_time
    
    if iter == 0:
        if 2*n <= 30:
            filename = f"./images/bad_order_crown_graph_greedy_{2*n}.png"
            plot_graph(G, coloring_greedy, filename)
        colors_nr = len(set(coloring_greedy))
        greedy_colors.append(colors_nr)
        print(f"Greedy used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_dsatur = dsatur.dsatur_coloring(graph)
    end_time = time.time()
    dsatur_time = end_time - start_time
    
    if iter == 0:
        if 2*n <= 30:
            filename = f"./images/bad_order_crown_graph_dsatur_{2*n}.png"
            plot_graph(G, coloring_dsatur, filename)
        colors_nr = len(set(coloring_dsatur))
        dsatur_colors.append(colors_nr)
        print(f"Dsatur used {colors_nr} colors.")
    
    times = [backtracking_time, greedy_time, dsatur_time]
    return times
    
############################# good order chordal graph #############################
def good_order_chordal_graph(iter):
    graph = read_graph_from_file("./in/manual/good_order_chordal_graph.in")
    
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    if nx.is_chordal(G):
        if iter == 0:
            print(f"Well ordered nodes in chordal graph with {len(graph)} nodes:")
            display_graph(graph)
        
        start_time = time.time()
        coloring_backtracking = backtr.backtr_optimal(graph)
        end_time = time.time()
        backtracking_time = end_time - start_time
        
        if iter == 0:
            plot_graph(G, coloring_backtracking, "./images/good_order_chordal_graph_backtracking.png")
            colors_nr = len(set(coloring_backtracking))
            print(f"Backtracking used {colors_nr} colors.")
        
        start_time = time.time()
        coloring_greedy = greedy.greedy_coloring(graph)
        end_time = time.time()
        greedy_time = end_time - start_time
        
        if iter == 0:
            plot_graph(G, coloring_greedy, "./images/good_order_chordal_graph_greedy.png")
            colors_nr = len(set(coloring_greedy))
            print(f"Greedy used {colors_nr} colors.")
        
        start_time = time.time()
        coloring_dsatur = dsatur.dsatur_coloring(graph)
        end_time = time.time()
        dsatur_time = end_time - start_time
        
        if iter == 0:
            plot_graph(G, coloring_dsatur, "./images/good_order_chordal_graph_dsatur.png")
            colors_nr = len(set(coloring_dsatur))
            print(f"Dsatur used {colors_nr} colors.")
    else:
        print("Graph is not chordal")
        
    times = [backtracking_time, greedy_time, dsatur_time]
    return times
        
############################# bad order chordal graph #############################
def bad_order_chordal_graph(iter):
    graph = read_graph_from_file("./in/manual/bad_order_chordal_graph.in")
    
    G = nx.Graph()
    for node, neighbors in enumerate(graph):
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    if nx.is_chordal(G):
        if iter == 0:
            print(f"Bad ordered nodes in chordal graph with {len(graph)} nodes:")
            display_graph(graph)
        
        start_time = time.time()
        coloring_backtracking = backtr.backtr_optimal(graph)
        end_time = time.time()
        backtracking_time = end_time - start_time
        
        if iter == 0:
            plot_graph(G, coloring_backtracking, "./images/bad_order_chordal_graph_backtracking.png")
            colors_nr = len(set(coloring_backtracking))
            print(f"Backtracking used {colors_nr} colors.")
        
        start_time = time.time()
        coloring_greedy = greedy.greedy_coloring(graph)
        end_time = time.time()
        greedy_time = end_time - start_time
        
        if iter == 0:
            plot_graph(G, coloring_greedy, "./images/bad_order_chordal_graph_greedy.png")
            colors_nr = len(set(coloring_greedy))
            print(f"Greedy used {colors_nr} colors.")
        
        start_time = time.time()
        coloring_dsatur = dsatur.dsatur_coloring(graph)
        end_time = time.time()
        dsatur_time = end_time - start_time
        
        if iter == 0:
            plot_graph(G, coloring_dsatur, "./images/bad_order_chordal_graph_dsatur.png")
            colors_nr = len(set(coloring_dsatur))
            print(f"Dsatur used {colors_nr} colors.")
    else:
        print("Graph is not chordal") 
        
    times = [backtracking_time, greedy_time, dsatur_time]
    return times
    
############################# complete graph #############################
def complete_graph(n, iter):
    filename = f"./in/complete_graph_{n}.in"
    graph = read_graph_from_file(filename)
    
    if iter == 0 and n <= 30:
        print(f"Complete graph with {len(graph)} nodes:")
        display_graph(graph)
        
        if 2*n <= 30:
            G = nx.Graph()
            for node, neighbors in enumerate(graph):
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)
    
    start_time = time.time()
    coloring_backtracking = backtr.backtr_optimal(graph)
    end_time = time.time()
    backtracking_time = end_time - start_time
    
    if iter == 0 and n <= 30:
        filename = f"./images/complete_graph_backtracking_{n}.png"
        plot_graph(G, coloring_backtracking, filename)
        colors_nr = len(set(coloring_backtracking))
        backtracking_colors.append(colors_nr)
        print(f"Backtracking used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_greedy = greedy.greedy_coloring(graph)
    end_time = time.time()
    greedy_time = end_time - start_time
    
    if iter == 0 and n <= 30:
        filename = f"./images/complete_graph_greedy_{n}.png"
        plot_graph(G, coloring_greedy, filename)
        colors_nr = len(set(coloring_greedy))
        greedy_colors.append(colors_nr)
        print(f"Greedy used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_dsatur = dsatur.dsatur_coloring(graph)
    end_time = time.time()
    dsatur_time = end_time - start_time
    
    if iter == 0 and n <= 30:
        filename = f"./images/complete_graph_dsatur_{n}.png"
        plot_graph(G, coloring_dsatur, filename)
        colors_nr = len(set(coloring_dsatur))
        dsatur_colors.append(colors_nr)
        print(f"Dsatur used {colors_nr} colors.")
        
    times = [backtracking_time, greedy_time, dsatur_time]
    return times
    
############################# random graph #############################
def random_graph(n, iter):
    filename = f"./in/random_graph_{n}.in"
    graph = read_graph_from_file(filename)
    
    if iter == 0:
        print(f"Random graph with {len(graph)} nodes:")
        display_graph(graph)
        
        if n <= 30:
            G = nx.Graph()
            for node, neighbors in enumerate(graph):
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)      
    
    start_time = time.time()
    coloring_backtracking = backtr.backtr_optimal(graph)
    end_time = time.time()
    backtracking_time = end_time - start_time
    
    if iter == 0:
        if n <= 30:
            filename = f"./images/random_graph_backtracking_{n}.png"
            plot_graph(G, coloring_backtracking, filename)
        colors_nr = len(set(coloring_backtracking))
        backtracking_colors.append(colors_nr)
        print(f"Backtracking used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_greedy = greedy.greedy_coloring(graph)
    end_time = time.time()
    greedy_time = end_time - start_time
    
    if iter == 0:
        if n <= 30:
            filename = f"./images/random_graph_greedy_{n}.png"
            plot_graph(G, coloring_greedy, filename)
        colors_nr = len(set(coloring_greedy))
        greedy_colors.append(colors_nr)
        print(f"Greedy used {colors_nr} colors.")
    
    start_time = time.time()
    coloring_dsatur = dsatur.dsatur_coloring(graph)
    end_time = time.time()
    dsatur_time = end_time - start_time
    
    if iter == 0:
        if n <= 30:
            filename = f"./images/random_graph_dsatur_{n}.png"
            plot_graph(G, coloring_dsatur, filename)
        colors_nr = len(set(coloring_dsatur))
        dsatur_colors.append(colors_nr)
        print(f"Dsatur used {colors_nr} colors.")
    
    times = [backtracking_time, greedy_time, dsatur_time]
    return times
    
def main():
    global backtracking_colors
    global greedy_colors
    global dsatur_colors
    nodes_range = []
    backtracking_times = []
    greedy_times = []
    dsatur_times = []
    
    # crown graphs with 2*n vertices
    crown_gen.crown_generator(10, 20)
    for n in range(10, 20 + 1):
        nodes_range.append(2*n)
        # run test 5 times 
        time_backtracking = 0
        time_greedy = 0
        time_dsatur = 0
        for i in range(5):
            times = good_order_crown_graph(n, i)
            time_backtracking += times[0]
            time_greedy += times[1]
            time_dsatur += times[2]
        backtracking_times.append(time_backtracking / 5 * 1000)
        greedy_times.append(time_greedy / 5 * 1000)
        dsatur_times.append(time_dsatur / 5 * 1000)
        print(f"Backtracking time: {time_backtracking / 5:.6f}")
        print(f"Greedy time: {time_greedy / 5:.6f}")
        print(f"DSatur time: {time_dsatur / 5:.6f}\n")
    plot_execution_time_vs_nodes(nodes_range, backtracking_times, greedy_times, dsatur_times, "graf coroana indexat favorabil")
    plot_colors_used_vs_nodes(nodes_range, backtracking_colors, greedy_colors, dsatur_colors, "graf coroana indexat favorabil")
    
    nodes_range.clear()
    backtracking_times.clear()
    greedy_times.clear()
    dsatur_times.clear()
    backtracking_colors.clear()
    greedy_colors.clear()
    dsatur_colors.clear()
    for n in range(10, 20 + 1):
        nodes_range.append(2*n)
        # run test 5 times
        time_backtracking = 0
        time_greedy = 0
        time_dsatur = 0
        for i in range(5):
            times = bad_order_crown_graph(n, i)
            time_backtracking += times[0]
            time_greedy += times[1]
            time_dsatur += times[2]
        backtracking_times.append(time_backtracking / 5 * 1000)
        greedy_times.append(time_greedy / 5 * 1000)
        dsatur_times.append(time_dsatur / 5 * 1000)
        print(f"Backtracking time: {time_backtracking / 5:.6f}")
        print(f"Greedy time: {time_greedy / 5:.6f}")
        print(f"DSatur time: {time_dsatur / 5:.6f}\n")
    plot_execution_time_vs_nodes(nodes_range, backtracking_times, greedy_times, dsatur_times, "graf coroana indexat nefavorabil")
    plot_colors_used_vs_nodes(nodes_range, backtracking_colors, greedy_colors, dsatur_colors, "graf coroana indexat nefavorabil")
       
    # chordal graphs
    nodes_range.clear()
    backtracking_times.clear()
    greedy_times.clear()
    dsatur_times.clear()
    backtracking_colors.clear()
    greedy_colors.clear()
    dsatur_colors.clear()
    for i in range(5):
        times = good_order_chordal_graph(i)
        time_backtracking += times[0]
        time_greedy += times[1]
        time_dsatur += times[2]
    print(f"Backtracking time: {time_backtracking / 5:.6f}")
    print(f"Greedy time: {time_greedy / 5:.6f}")
    print(f"DSatur time: {time_dsatur / 5:.6f}\n")
    
    nodes_range.clear()
    backtracking_times.clear()
    greedy_times.clear()
    dsatur_times.clear()
    backtracking_colors.clear()
    greedy_colors.clear()
    dsatur_colors.clear()
    for i in range(5):
        times = bad_order_chordal_graph(i)
        time_backtracking += times[0]
        time_greedy += times[1]
        time_dsatur += times[2]
    print(f"Backtracking time: {time_backtracking / 5:.6f}")
    print(f"Greedy time: {time_greedy / 5:.6f}")
    print(f"DSatur time: {time_dsatur / 5:.6f}\n")
    
    #random graphs
    nodes_range.clear()
    backtracking_times.clear()
    greedy_times.clear()
    dsatur_times.clear()
    backtracking_colors.clear()
    greedy_colors.clear()
    dsatur_colors.clear()
    rand_gen.random_graph_generator(20, 30, 0.3)
    for n in range(20, 30 + 1):
        nodes_range.append(n)
        time_backtracking = 0
        time_greedy = 0
        time_dsatur = 0
        for i in range(5):
            times = random_graph(n, i)
            time_backtracking += times[0]
            time_greedy += times[1]
            time_dsatur += times[2]
        backtracking_times.append(time_backtracking / 5 * 1000)
        greedy_times.append(time_greedy / 5 * 1000)
        dsatur_times.append(time_dsatur / 5 * 1000)
        print(f"Backtracking time: {time_backtracking / 5:.6f}")
        print(f"Greedy time: {time_greedy / 5:.6f}")
        print(f"DSatur time: {time_dsatur / 5:.6f}\n")
    plot_execution_time_vs_nodes(nodes_range, backtracking_times, greedy_times, dsatur_times, "graf aleator")
    plot_colors_used_vs_nodes(nodes_range, backtracking_colors, greedy_colors, dsatur_colors, "graf aleator")
        
    # complete graphs with n vertices
    nodes_range.clear()
    backtracking_times.clear()
    greedy_times.clear()
    dsatur_times.clear()
    backtracking_colors.clear()
    greedy_colors.clear()
    dsatur_colors.clear()
    complete_gen.complete_graph_generator(5, 10)
    for n in range(5, 10 + 1):
        nodes_range.append(n)
        time_backtracking = 0
        time_greedy = 0
        time_dsatur = 0
        for i in range(5):
            times = complete_graph(n, i)
            time_backtracking += times[0]
            time_greedy += times[1]
            time_dsatur += times[2]
        backtracking_times.append(time_backtracking / 5 * 1000)
        greedy_times.append(time_greedy / 5 * 1000)
        dsatur_times.append(time_dsatur / 5 * 1000)
        print(f"Backtracking time: {time_backtracking / 5:.6f}")
        print(f"Greedy time: {time_greedy / 5:.6f}")
        print(f"DSatur time: {time_dsatur / 5:.6f}\n")
    plot_execution_time_vs_nodes(nodes_range, backtracking_times, greedy_times, dsatur_times, "graf complet")
    plot_colors_used_vs_nodes(nodes_range, backtracking_colors, greedy_colors, dsatur_colors, "graf complet")

if __name__ == "__main__":
    main()