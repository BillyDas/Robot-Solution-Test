# Definitions
# #number of rows and columns
# R,C = 99
# #robot matrix of size RXC
# m = 1
# rs, sc = 0
# rq, cq = 0
# dr = [-1,+1,0,0]
# dc = [0,0,+1,-1]
# move_count = 0
# node_left_in_later = 1
# nodes_in_next_layer = 0
# reached_end = false
# visited =
#

# +10 ti
# This is realy stupid.
# graph = {
#         '0': ['1, 10'], '1': ['0, 11, 2'], '2': ['1, 3, 12'], '3': ['2, 4, 13'], '4': ['14, 3, 5'], '5': ['15,4,6'], '6': ['5,16,7'], '7': ['6,17,8'], '8': ['7,18,9'], '9': ['8,19'],
#         '10': ['0,11,20'], '11': ['1,10,21,12'], '12': ['2,22,13,11'], '13': ['3,23,12,14'], '14': ['4,24,13,15'], '15': ['5,25,14,16'], '16': ['6,26,15,17'], '17': ['7,27,16,18'], '18': ['8,28,17,19'], '19': ['9,18,29'],
#         '20': ['10,21,30'], '21': ['11,20,31,22'], '22': ['12,32,23,21'], '23': ['13,33,22,24'], '24': ['14,34,23,25'], '25': ['15,35,24,26'], '26': ['16,36,25,27'], '27': ['17,37,26,28'], '28': ['18,38,27,29'], '29': ['19,28,39'],
#         '30': ['20,31,40'], '31': ['21,30,41,32'], '32': ['22,42,33,41'], '33': ['23,43,32,34'], '34': ['24,44,33,35'], '25': ['15,35,24,26'], '26': ['16,36,25,27'], '27': ['17,37,26,28'], '28': ['18,38,27,29'], '29': ['19,28,39'],
#         }


x = 0
y = 0
dir = 0

def sortdata(data):
    #splits data by comma
    sorted = data.split(",")
    return sorted

def Move(movement):
    global dir
    global x
    global y
    #for each thing in the sortedMovement Array
    for move in movement:
        #if the selected cell of the array has an "R" in it, it will trigger fucntion Direction, This will turn the bot 90Degrees right
        if "R" in move:
            Direction(move, "R")

        #if the selected cell of the array has an "l" in it, it will trigger fucntion Direction, this iwll turn the bot 90 Degrees left
        if "L" in move:
            Direction(move, "L")

        if "F" in move:
            res = int(move[1:])
            if dir == 0:
                y += res
            elif dir == 1:
                x += res
            elif dir == 2:
                y -= res
            elif dir == 3:
                x -= res

        if "B" in move:
            res = int(move[1:])
            if dir == 0:
                y -= res
            elif dir == 1:
                x -= res
            elif dir == 2:
                y += res
            elif dir == 3:
                x += res

def disFromHome(x, y):
    ans = abs(x) + abs(y)
    return ans





#Master function for sorting out dir.
# North = 0
# East = 1
# South = 2
# West = 3
def Direction(move, turnDiection):
    global dir
    res = int(move[1:])
    if turnDiection == "L":
        dir -= res
    elif turnDiection == "R":
        dir += res
    dir = dir % 4


    # if dir == 3 & turnDiection == "R"
    #     dir = 0
    #     return
    # elif dir == 0 & turnDiection == "L"
    #     dir = 3
    #     return
    # elif turnDiection == "L"
    #     dir -= 1
    #     return
    # elif turnDiection == "R"
    #     dir += 1
    #     return


# def solveDistance():
#     rq.



#Program Starts
print("Program Start")
# Program asks for users input assumign its correct
data = inputdata = input("Please input Movement Commands in comma separated form eg 'F1,R1,B2,L1,B3': ")
# sorts data
sortedData = sortdata(data)
Move(sortedData)
ans = disFromHome(x, y)
print ("the minimum amount of distance to get back to the starting point is", ans)
