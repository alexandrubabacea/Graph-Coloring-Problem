import backtracking_graph_coloring_decision as backtr_d

def backtr_optimal(graph):
    for k in range(1, len(graph) + 1):
        coloring = [-1] * len(graph)
        solution, coloring = backtr_d.backtrack_coloring(graph, k, coloring, 0)
        
        if solution:
            return coloring