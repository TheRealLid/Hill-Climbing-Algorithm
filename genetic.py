import copy
import board
import random
import timeit

start = timeit.default_timer()


# creates a string representation of the current board state
def makeString(arr):
    string = ''
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i][j] == 1:
                string = string + str(i)
                string = string + str(j)
    return string


# best case is 20
def nonAttackingPairs(arr):
    hVal = 0
    size = int(len(arr) / 2)
    pairs = []
    index = 0
    for i in range(0, size):
        p = (arr[index], arr[index + 1])
        pairs.append(p)
        index += 2
    # print(pairs)
    for i in range(0, size):
        for j in range(0, size):

            if pairs[j][0] != pairs[i][0] and pairs[j][1] != pairs[i][1]:
                if comparePairs(size, pairs[j], pairs[i]):
                    hVal += 1

    return hVal


# returns true if the queens are not attacking
def comparePairs(size, pair1, pair2):
    i = int(pair1[0])
    j = int(pair1[1])
    i_2 = int(pair2[0])
    j_2 = int(pair2[1])
    # checks rows/columns
    if i == i_2 or j == j_2:
        return False
    # checks diagonals
    for k in range(1, size):
        # searches up right
        if (i - k) == i_2 and (j + k) == j_2:
            return False
        # searches up left
        elif (i - k) == i_2 and (j - k) == j_2:
            return False
        # searches down right
        elif (i + k) == i_2 and (j + k) == j_2:
            return False
        # searches down left
        elif (i + k) == i_2 and (j - k) == j_2:
            return False
    return True


states = []
maps = []

# sets up the 8 boards as strings within the list states
for i in range(0, 8):
    b = board.Board(5)
    states.append(makeString(b.map))
greatestHVal = 0
loops = 0
restarts = 0
# if greatestHVal is 20, we found our best case solution
while greatestHVal != 20:
    if loops > 60:
        loops = 0
        restarts += 1
        for i in range(0, 8):
            b = board.Board(5)
            states.append(makeString(b.map))
    loops += 1
    hVals = []
    sumOfHVals = 0
    # creates the list of heuristic values
    for i in range(0, 8):
        hVals.append(nonAttackingPairs(states[i]))
        sumOfHVals += hVals[i]
    # sorts the list oif heuristic values from high to low as well as adjusts states so the index line up
    for i in range(0, 8):
        for j in range(0, 8):
            temp = hVals[j]
            tempState = states[j]
            if hVals[j] < hVals[i]:
                hVals[j] = hVals[i]
                hVals[i] = temp
                states[j] = states[i]
                states[i] = tempState

    normalizedVals = []
    # Selection
    # normalizes the values
    for i in range(0, 8):
        normalizedVals.append(hVals[i] / sumOfHVals)
    # selection takes place here based on random chance
    newStates = []
    for i in range(0, len(normalizedVals)):
        r = random.uniform(0, 1)
        if r < normalizedVals[0]:
            newStates.append(states[0])
        elif r < normalizedVals[1] + normalizedVals[0]:
            newStates.append(states[1])
        elif r < normalizedVals[2] + normalizedVals[1] + normalizedVals[0]:
            newStates.append(states[2])
        elif r < normalizedVals[3] + normalizedVals[2] + normalizedVals[1] + normalizedVals[0]:
            newStates.append(states[3])
        elif r < normalizedVals[4] + normalizedVals[3] + normalizedVals[2] + normalizedVals[1] + normalizedVals[0]:
            newStates.append(states[4])
        elif r < normalizedVals[5] + normalizedVals[4] + normalizedVals[3] + normalizedVals[2] + normalizedVals[1] + \
                normalizedVals[0]:
            newStates.append(states[5])
        elif r < normalizedVals[6] + normalizedVals[5] + normalizedVals[4] + normalizedVals[3] + normalizedVals[2] + \
                normalizedVals[1] + normalizedVals[0]:
            newStates.append(states[6])
        else:
            newStates.append(states[7])
    states = newStates

    # cross over
    index = 0
    for i in range(0, 4):
        if random.randrange(0, 2) == 1:
            r = random.randrange(0, len(states[0]) - 2)
            temp = states[index]
            states[index] = states[index][0:r] + states[index + 1][r:]
            states[index + 1] = states[index + 1][0:r] + temp[r:]
        index += 2

    # mutation
    for i in range(0, 8):
        if random.randrange(0, 2) == 1:
            location = random.randrange(0, 9)
            r = random.randrange(0, 5)
            states[i] = states[i][:location] + str(r) + str(states[i][location + 1:])

    greatestHVal = 0
    sumOfHVals = 0
    endingIndex = 0
    hVals = []
    for i in range(0, 8):
        hVals.append(nonAttackingPairs(states[i]))
        sumOfHVals += hVals[i]
    for i in range(0, len(hVals)):
        if greatestHVal < hVals[i]:
            greatestHVal = hVals[i]
            endingIndex = i

size = int(len(states[endingIndex]) / 2)
pairs = []
index = 0
for i in range(0, size):
    p = (states[endingIndex][index], states[endingIndex][index + 1])
    pairs.append(p)
    index += 2

arr = [['-' for j in range(5)] for i in range(5)]

for i in range(0, 5):
    y = int(pairs[i][0])
    x = int(pairs[i][1])
    arr[y][x] = 1

stop = timeit.default_timer()
print("Running time: ", str(int((stop - start) * 1000)) + "ms")
print("# of restarts: " + str(restarts))
for i in range(0, 5):
    for j in range(0, 5):
        if j != 4:
            print(arr[i][j], end=" ")
        else:
            print(arr[i][j])
