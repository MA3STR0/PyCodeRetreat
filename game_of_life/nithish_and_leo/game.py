# plotting only works in the Jupyter Notebook

import random
import time
from IPython.display import display, clear_output, HTML


class GameOfLife():
    def __init__(self, size, gliderOption=None):
        self.size = size
        self.gameMatrix = []
        if gliderOption == 1:
            assert(self.size >= 10)
            for row in range(self.size):
                self.gameMatrix.append([0]*self.size)
            self.gameMatrix[0][1] = 1
            self.gameMatrix[1][2] = 1
            self.gameMatrix[2][0] = 1
            self.gameMatrix[2][1] = 1
            self.gameMatrix[2][2] = 1
        elif gliderOption == 2:
            self.gameMatrix =[
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            for n in range(27):
                self.gameMatrix.append([0] * 36)
            self.size = 36
        else:
            for row in range(self.size):
                self.gameMatrix.append([0]*self.size)
            for row in range(self.size):
                for col in range(self.size):
                    probLife = random.random()
                    if probLife >= 0.5:
                        self.gameMatrix[row][col] = 1

    def printGame(self):
        for row in self.gameMatrix:
            print(row)

    def calculateAliveNeighbours(self, row, col):
        neigh_row_min = max(row-1, 0)
        neigh_row_max = min(row+1, self.size-1)
        neigh_col_min = max(col-1, 0)
        neigh_col_max = min(col+1, self.size-1)
        countAlive = 0
        for neigh_row in range(neigh_row_min, neigh_row_max+1):
            for neigh_col in range(neigh_col_min, neigh_col_max+1):
                if neigh_col == col and neigh_row == row:
                    pass
                else:
                    countAlive += self.gameMatrix[neigh_row][neigh_col]
        return countAlive

    def updateGame(self):
        aliveNeighbours = []
        for row in range(self.size):
            row_values = []
            aliveNeighbours.append(row_values)
            for col in range(self.size):
                row_values.append(self.calculateAliveNeighbours(row, col))
        print('Updated Matrix')
        for row in range(self.size):
            for col in range(self.size):
                if self.gameMatrix[row][col]:
                    if aliveNeighbours[row][col] < 2 or aliveNeighbours[row][col] > 3:
                        self.gameMatrix[row][col] = 0
                else:
                    if aliveNeighbours[row][col] == 3:
                        self.gameMatrix[row][col] = 1
        # self.plotGame()

    def plotGame(self):
        black = ("<td style='border: 1px solid black; background: black;"
                 "width: 20px; height: 20px'></td>")
        white = ("<td style='border: 1px solid black; background: white;"
                 "width: 20px; height: 20px'></td>")
        table = ""
        for row_array in self.gameMatrix:
            row = ""
            for entry in row_array:
                row += black if entry else white
            table += "<tr>{row}</tr>".format(row=row)
        clear_output()
        display(HTML("<table>{table}</table>".format(table=table)))


aGame = GameOfLife(20, gliderOption=2)
aGame.plotGame()
while True:
    aGame.updateGame()
    aGame.plotGame()
    time.sleep(0.25)
