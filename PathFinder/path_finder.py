from maze.maze import Maze
from graph.dfs import dfs

def path_finder(maze):
    maze = maze.split('\n')
    maze = Maze(maze)
    G = maze.get_graph_from_maze()

    color = {i: "white" for i in G.keys()}
    pred = {i: None for i in G.keys()}
    cc = {i: None for i in G.keys()}
    cc_num = [0]
    dfs(G, color, pred, cc, cc_num)

    start_idx = 0
    exit_idx = maze.n * maze.m - 1

    if start_idx not in G.keys() or exit_idx not in G.keys():
        return False
    elif cc[start_idx] != cc[exit_idx]:
        return False
    else:
        return True
