from table import Table
import time
import sys
from progbar import ProgressBar
class Alignment:
    def __init__(self):
        self.x = ""
        self.y = ""
        self.tab = Table()

    def initialize(self, a, b):
        #print(a)
        #print(b)
        self.x = a
        self.y = b

        sizeX = len(a)
        sizeY = len(b)

        cur_time = time.time()
        progress_bar = ProgressBar(100)
        print("allocating memory...", end='', flush=True)
        self.tab.resize(len(self.x)+1, len(self.y)+1)
        print("done")
        print("computing alignment...\n", end='', flush=True)

        for i in range(sizeX+1):
            self.tab[i,0] = i
        for i in range(sizeY+1):
            self.tab[0,i] = i

        for i in range(1,sizeX+1):
            progress_bar.print_bar(i*100/len(self.x)) 
            for j in range(1,sizeY+1):
                if self.x[i-1] == self.y[j-1]:
                    cost = 0
                else:
                    cost = 1
                self.tab[i,j] = min(
                    self.tab[i-1, j] + 1,
                    self.tab[i, j-1] + 1,
                    self.tab[i-1, j-1] + cost
                )
        # FILL IN
        # If you have a loop index i that goes to n, you can output a text
        # "progress bar" that shows progress through the loop by calling
        #  progress_bar.print_bar(i*100/ n)
        
        print(f'\n Total Time : {time.time()- cur_time:.2f}s')
        
    def distance(self):
        return self.tab[len(self.x), len(self.y)]
