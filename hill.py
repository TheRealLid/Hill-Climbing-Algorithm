import copy
import board
import timeit

start = timeit.default_timer()
current = board.Board(5)
current.fitness()
original = copy.deepcopy(current)
loop = 0
restart = 0
mostExpensive = 0


pair = (0, 0)
for i in range(0, current.n_queen):
    for j in range(0, current.n_queen):
        if current.map[i][j] == 1:
            p = (i, j)
            cost = current.expensiveQueen(p)
            if cost >= mostExpensive:
                mostExpensive = cost
                pair = (i, j)

# if the most expensive queen is 0, we found the solution
while mostExpensive != 0:
    if loop >= current.n_queen*2:
        current = board.Board(5)
        current.fitness()

        for i in range(0, current.n_queen):
            for j in range(0, current.n_queen):
                if current.map[i][j] == 1:
                    p = (i, j)
                    cost = current.expensiveQueen(p)
                    if cost >= mostExpensive:
                        mostExpensive = cost
                        pair = (i, j)
        loop = 0
        restart += 1
    loop += 1

    temp1 = copy.deepcopy(current)
    queenCords = []
    mostExpensive = 0

    i_index = pair[0]
    j_index = pair[1]

    temp1.map[i_index][j_index] = 0

    arr = []
    # will be changed to True if a 1 can be placed at the i and j index
    i_up = False
    i_down = False
    j_left = False
    j_right = False
    ij_upLeft = False
    ij_upRight = False
    ij_downLeft = False
    ij_downRight = False

    if i_index - 1 >= 0:
        i_up = True

    if i_index + 1 <= 4:
        i_down = True

    if j_index - 1 >= 0:
        j_left = True

    if j_index + 1 <= 4:
        j_right = True

    if i_up and j_right:
        ij_upRight = True

    if i_up and j_left:
        ij_upLeft = True

    if i_down and j_right:
        ij_downRight = True

    if i_down and j_left:
        ij_downLeft = True
    # places the 1 in its new spot and adds the updated matrix to an array
    for i in range(0, 8):
        if ij_upLeft and temp1.map[i_index - 1][j_index - 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index - 1][j_index - 1] = 1
            arr.append(temp)
            ij_upLeft = False

        elif ij_upRight and temp1.map[i_index - 1][j_index + 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index - 1][j_index + 1] = 1
            arr.append(temp)
            ij_upRight = False

        elif ij_downLeft and temp1.map[i_index + 1][j_index - 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index + 1][j_index - 1] = 1
            arr.append(temp)
            ij_downLeft = False

        elif ij_downRight and temp1.map[i_index + 1][j_index + 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index + 1][j_index + 1] = 1
            arr.append(temp)
            ij_downRight = False

        elif i_up and temp1.map[i_index - 1][j_index] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index - 1][j_index] = 1
            arr.append(temp)
            i_up = False

        elif i_down and temp1.map[i_index + 1][j_index] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index + 1][j_index] = 1
            arr.append(temp)
            i_down = False

        elif j_left and temp1.map[i_index][j_index - 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index][j_index - 1] = 1
            arr.append(temp)
            j_left = False

        elif j_right and temp1.map[i_index][j_index + 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index][j_index + 1] = 1
            arr.append(temp)
            j_right = False

    bestFit = copy.deepcopy(current)
    bestFit.fit = 0
    bestFit.fitness()
    for i in range(0, len(arr)):
        arr[i].fit = 0
        arr[i].fitness()
        if arr[i].get_fit() <= bestFit.get_fit():
            bestFit = copy.deepcopy(arr[i])

    # finds the most expensive so the program knows to end if the most expensive is 0 aswell as to be used in next loop
    current = copy.deepcopy(bestFit)
    mostExpensive = 0
    for i in range(0, current.n_queen):
        for j in range(0, current.n_queen):
            if current.map[i][j] == 1:
                p = (i, j)
                cost = current.expensiveQueen(p)
                if cost >= mostExpensive:
                    mostExpensive = cost
                    pair = (i, j)

stop = timeit.default_timer()
print("Running time: ", str(int((stop - start) * 1000)) + "ms")
print("# of restarts: " + str(restart))
for i in range(0, current.n_queen):
    for j in range(0, current.n_queen):
        if current.map[i][j] == 1:
            if j != current.n_queen-1:
                print("1", end=" ")
            else:
                print("1 ")
        else:
            if j != current.n_queen-1:
                print("-", end=" ")
            else:
                print("- ")

