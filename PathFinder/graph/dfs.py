def dfs(G, color, pred, cc, cc_num):
    for v in G.keys():
        if color[v] == "white":
            dfs_visit(G, v, color, pred, cc, cc_num)

def dfs_visit(G, u, color, pred, cc, cc_num):
    '''
        G      - graph
        u      - current node
        color  - node color
        pred   - node predecessor
        cc     - connectivity components
        cc_num - connectivity components num
    '''
    color[u] = "gray"
    if cc[u] is None:
        cc_num[0] += 1
        cc[u] = cc_num[0]

    for v in G[u]:
        if color[v] == "white":
            pred[v] = u
            cc[v] = cc[u]
            dfs_visit(G, v, color, pred, cc, cc_num)

    color[u] = "black"