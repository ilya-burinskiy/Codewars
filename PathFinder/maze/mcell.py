class MazeCell:
    
    def __init__(self, i, j, idx, char: str):
        self._i = i
        self._j = j
        self._idx = idx
        self._type = "empty" if char == '.' else "wall"

    @property
    def i(self):
        return self._i

    @property
    def j(self):
        return self._j

    @property
    def idx(self):
        return self._idx
    
    @property
    def type(self):
        return self._type

    def __repr__(self):
        return "({},{})".format(self._i, self._j)

    def __hash__(self):
        return hash(self._idx)