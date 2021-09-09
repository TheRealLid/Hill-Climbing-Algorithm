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
        self.fit = 0
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

    def expensiveQueen(self):
        pair = (0, 0)
        mostExpensive = 0
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    temp = 0
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            temp += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            temp += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            temp += 1
                    print("temp: = " + str(temp))
                    print("pair: " + str(i) + "," + str(j))
                    if random.randrange(0, 11) >= 0:
                        if mostExpensive < temp:
                            mostExpensive = temp
                            print("(normal)most expensive: " + str(mostExpensive))
                            pair = (i, j)
                        #elif mostExpensive == temp:
                            #if random.randrange(0, 2) == 1:
                                #pair = (i, j)
                                #print("(equal swap)most expensive: " + str(mostExpensive))
                   # else:
                        #pair = (i, j)
                       # print("(random)most expensive: " + str(mostExpensive))


        return pair

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
