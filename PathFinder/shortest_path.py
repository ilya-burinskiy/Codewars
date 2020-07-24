from graph.bfs import bfs

def shortest_path(G, start_idx, exit_idx):
    destinations = bfs(G, start_idx)
    steps_num = destinations[exit_idx]

    if steps_num == float("inf"):
        return False
    else:
        return steps_num