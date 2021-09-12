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
    def fitness(self):
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

    def expensiveQueen(self, pair):
        i = pair[0]
        j = pair[1]
        cost = 0
        for k in range(1, self.n_queen):
            # searches right
            if j + k < self.n_queen and self.map[i][j + k] == 1:
                cost += 1
            # searches left
            if j - k >= 0 and self.map[i][j - k] == 1:
                cost += 1
            # searches down
            if i + k < self.n_queen and self.map[i+k][j] == 1:
                cost += 1
            # searches up
            if i - k >= 0 and self.map[i-k][j] == 1:
                cost += 1
            # searches up right
            if i - k >= 0 and j + k < self.n_queen and self.map[i-k][j+k] == 1:
                cost += 1
            # searches up left
            if i - k >= 0 and j - k >= 0 and self.map[i-k][j-k] == 1:
                cost += 1
            # searches down right
            if i + k < self.n_queen and j + k < self.n_queen and self.map[i+k][j+k] == 1:
                cost += 1
            # searches down left
            if i + k < self.n_queen and j - k >= 0 and self.map[i+k][j-k] == 1:
                cost += 1
        return cost


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
    print("running board")
    #test = Board(5)
    #test.fitness()
    #test.show()
