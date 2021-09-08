import copy
import board
current = board.Board(5)
current.fitness()
current.show()

i_index = 0
j_index = 0
for i in range(0, 5):
    if current.map[0][i] == 1:
        current.map[0][i] = 0
        j_index = i
        break
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
    temp = copy.deepcopy(current)
    if ij_upLeft and temp.map[i_index - 1][j_index - 1] != 1:
        temp.map[i_index - 1][j_index - 1] = 1
        arr.append(temp)
        ij_upLeft = False
        print("upLeft")

    elif ij_upRight and temp.map[i_index - 1][j_index + 1] != 1:
        temp.map[i_index - 1][j_index + 1] = 1
        arr.append(temp)
        ij_upRight = False
        print("upRight")

    elif ij_downLeft and temp.map[i_index + 1][j_index - 1] != 1:
        temp.map[i_index + 1][j_index - 1] = 1
        arr.append(temp)
        ij_downLeft = False
        print("downLeft")

    elif ij_downRight and temp.map[i_index + 1][j_index + 1] != 1:
        temp.map[i_index + 1][j_index + 1] = 1
        arr.append(temp)
        ij_downRight = False
        print("downRight")

    elif i_up and temp.map[i_index-1][j_index] != 1:
        temp.map[i_index-1][j_index] = 1
        arr.append(temp)
        i_up = False
        print("up")
    elif i_down and temp.map[i_index + 1][j_index] != 1:
        temp.map[i_index + 1][j_index] = 1
        arr.append(temp)
        i_down = False
        print("down")
    elif j_left and temp.map[i_index][j_index - 1] != 1:
        temp.map[i_index][j_index - 1] = 1
        arr.append(temp)
        j_left = False
        print("left")
    elif j_right and temp.map[i_index][j_index + 1] != 1:
        temp.map[i_index][j_index + 1] = 1
        arr.append(temp)
        j_right = False
        print("right")
print("length of arr = " + str(len(arr)))
for i in range(0, len(arr)):
    arr[i].fitness()
    arr[i].show()
