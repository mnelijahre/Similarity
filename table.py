class Table:
    def __init__(self, rows=0, cols=0):
        self.data = None
        if rows and cols: self.resize(rows,cols)

    def resize(self, a, b):
        self.data = [[0 for _ in range(b)] for _ in range(a)]
        
    def __getitem__(self,index):
        r,c = index
        return self.data[r][c]
    def __setitem__(self,index,w):
        r,c = index
        self.data[r][c] = w
