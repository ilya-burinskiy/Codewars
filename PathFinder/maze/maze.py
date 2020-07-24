import random
from .mcell import MazeCell

class Maze:

    def __init__(self, maze: str):
        self._M = []
        i = j = 0
        idx = 0
        for string in maze:
            row = []
            for char in string:
                row.append(MazeCell(i, j, idx, char))
                idx += 1
                j += 1
            j = 0
            self._M.append(row)
            i += 1

        self._m = len(self._M)
        self._n = len(self._M[0])


    def _out_of_range(self, i, j):
        if (i < 0 or i > self._m - 1 or
                j < 0 or j > self._m - 1):
            return True

        return False

    def _get_neighbours(self, cell: MazeCell):
        i, j = cell.i, cell.j 

        moves = 4
        di = [-1, 0, 1, 0]
        dj = [0, -1, 0, 1]

        neighbours = []
        for move in range(moves):
            new_i, new_j = i + di[move], j + dj[move]
            if self._out_of_range(new_i, new_j):
                continue
            if self._M[new_i][new_j].type == "empty":
                neighbours.append(self._M[new_i][new_j])

        return neighbours

    def get_graph_from_maze(self):
        G = {}
        for i in range(self._m):
            for j in range(self._n):
                cell = self._M[i][j]
                if cell.type == "empty":
                    cell_neighbours = self._get_neighbours(cell)
                    G[cell.idx] = []
                    for n in cell_neighbours:
                        G[cell.idx].append(n.idx)

        return G

    @property
    def m(self):
        return self._m

    @property
    def n(self):
        return self._n