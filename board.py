import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0

        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    # determines fitness rating for the current board state
    def fitness(self): # TODO modify this code to find most expensive queen
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit += 1

    # shows the matrix and fitness rating, requires fitness rating to be updated before hand
    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ", self.fit)

    # flips the state of board at position i, j
    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    # returns a 2d array containing the map/board
    def get_map(self):
        return self.map

    # returns the fitness rating, low is better
    def get_fit(self):
        return self.fit


if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()
