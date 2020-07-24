from queue import Queue

def bfs(G: dict, s: int):
    color = {i: "white" for i in G.keys() if i != s}
    destination = {i: float("inf") for i in G.keys() if i != s}

    color[s] = "gray"
    destination[s] = 0

    q = Queue()
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if color[v] == "white":
                color[v] = "gray"
                destination[v] = destination[u] + 1
                q.put(v)

        color[u] = "black"

    return destination