import copy
import board

current = board.Board(5)
current.fitness()
current.show()
original = copy.deepcopy(current)
loop = 0
restart = 0
while loop != 1:
    if loop >= 100:
        current = copy.deepcopy(original)
        current.fitness()
        loop = 0
        restart += 1
    loop += 1

    temp1 = copy.deepcopy(current)
    queenCords = []

    for i in range(0, current.n_queen):
        for j in range(0, current.n_queen):
            if current.map[i][j] == 1:
                p = (i, j)
                queenCords.append(p)

    print(p)
    print(current.expensiveQueen(p))
    pair = (0, 0)
    i_index = pair[0]
    j_index = pair[1]
    print(pair)
    temp1.show()
    temp1.map[i_index][j_index] = 0

    arr = []

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

    for i in range(0, 8):
        if ij_upLeft and temp1.map[i_index - 1][j_index - 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index - 1][j_index - 1] = 1
            arr.append(temp)
            ij_upLeft = False
            # print("upLeft" + " " + str(i))

        elif ij_upRight and temp1.map[i_index - 1][j_index + 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index - 1][j_index + 1] = 1
            arr.append(temp)
            ij_upRight = False
            # print("upRight"  + " " + str(i))

        elif ij_downLeft and temp1.map[i_index + 1][j_index - 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index + 1][j_index - 1] = 1
            arr.append(temp)
            ij_downLeft = False
            # print("downLeft"  + " " + str(i))

        elif ij_downRight and temp1.map[i_index + 1][j_index + 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index + 1][j_index + 1] = 1
            arr.append(temp)
            ij_downRight = False
            # print("downRight" + " " + str(i))

        elif i_up and temp1.map[i_index - 1][j_index] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index - 1][j_index] = 1
            arr.append(temp)
            i_up = False
            # print("up" + " " + str(i))
        elif i_down and temp1.map[i_index + 1][j_index] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index + 1][j_index] = 1
            arr.append(temp)
            i_down = False
        # print("down" + " " + str(i))
        elif j_left and temp1.map[i_index][j_index - 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index][j_index - 1] = 1
            arr.append(temp)
            j_left = False
            # print("left" + " " + str(i))
        elif j_right and temp1.map[i_index][j_index + 1] != 1:
            temp = copy.deepcopy(temp1)
            temp.map[i_index][j_index + 1] = 1
            arr.append(temp)
            j_right = False
            # print("right" + " " + str(i))
    bestFit = copy.deepcopy(current)
    bestFit.fitness()
    for i in range(0, len(arr)):
        arr[i].fitness()
        if arr[i].get_fit() <= bestFit.get_fit():
            bestFit = copy.deepcopy(arr[i])
        # arr[i].show()

    # print("in loop show")
    current = copy.deepcopy(bestFit)
    # current.show()
    # print(current.fit)
print("restarts = " + str(restart))
current.fitness()
current.show()
