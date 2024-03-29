import copy
import board

current = board.Board(5)
current.fitness()
current.show()

while current.fit != 0:
    temp1 = copy.deepcopy(current)

    pair = current.expensiveQueen()
    i_index = pair[0]
    j_index = pair[1]
    temp1.map[i_index][j_index] = 0

    #print(pair)

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
        temp = copy.deepcopy(temp1)
        if ij_upLeft and temp.map[i_index - 1][j_index - 1] != 1:
            temp.map[i_index - 1][j_index - 1] = 1
            arr.append(temp)
            ij_upLeft = False
            # print("upLeft" + " " + str(i))

        elif ij_upRight and temp.map[i_index - 1][j_index + 1] != 1:
            temp.map[i_index - 1][j_index + 1] = 1
            arr.append(temp)
            ij_upRight = False
            # print("upRight"  + " " + str(i))

        elif ij_downLeft and temp.map[i_index + 1][j_index - 1] != 1:
            temp.map[i_index + 1][j_index - 1] = 1
            arr.append(temp)
            ij_downLeft = False
            # print("downLeft"  + " " + str(i))

        elif ij_downRight and temp.map[i_index + 1][j_index + 1] != 1:
            temp.map[i_index + 1][j_index + 1] = 1
            arr.append(temp)
            ij_downRight = False
            # print("downRight" + " " + str(i))

        elif i_up and temp.map[i_index - 1][j_index] != 1:
            temp.map[i_index - 1][j_index] = 1
            arr.append(temp)
            i_up = False
            # print("up" + " " + str(i))
        elif i_down and temp.map[i_index + 1][j_index] != 1:
            temp.map[i_index + 1][j_index] = 1
            arr.append(temp)
            i_down = False
            # print("down" + " " + str(i))
        elif j_left and temp.map[i_index][j_index - 1] != 1:
            temp.map[i_index][j_index - 1] = 1
            arr.append(temp)
            j_left = False
            # print("left" + " " + str(i))
        elif j_right and temp.map[i_index][j_index + 1] != 1:
            temp.map[i_index][j_index + 1] = 1
            arr.append(temp)
            j_right = False
            # print("right" + " " + str(i))
    #print(len(arr))
    bestFit = copy.deepcopy(current)
    for i in range(0, len(arr)):
        arr[i].fit = 0
        arr[i].fitness()
        if arr[i].fit <= bestFit.fit:
            bestFit = copy.deepcopy(arr[i])
    current = copy.deepcopy(bestFit)
    current.show()
    #print(current.fit)
current.show()