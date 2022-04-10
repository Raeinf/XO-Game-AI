

import sys
print(sys.setrecursionlimit(40000))


GameMap = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]
           ]


def Map_Changer(Map, Turn, po):
    m = []
    for i in Map:
        m.append(i.copy())
    m[po[0]][po[1]] = Turn
    return m


def Check_Win(GameMap):
    for i in range(3):
        if GameMap[i][0] == GameMap[i][1] == GameMap[i][2]:
            return GameMap[i][0]
        if GameMap[0][i] == GameMap[1][i] == GameMap[2][i]:
            return GameMap[0][i]
    if GameMap[2][0] == GameMap[1][1] == GameMap[0][2] or GameMap[2][2] == GameMap[1][1] == GameMap[0][0]:
        return GameMap[1][1]
    draw = 0
    for i in GameMap:
        for j in i:
            if j != "*":
                draw += 1
    if draw == 9:
        return "Draw"


def Ai():
    global GameMap
    Xwins = []
    TricWin = []
    Draws = []

    def Think(Map, route=[]):
        Flag = None
        for i in range(3):
            for j in range(3):
                if Map[i][j] == "*":
                    r = []
                    NewMap = Map_Changer(Map, "X", (i, j))
                    r.append((i, j, "X"))
                    if Check_Win(NewMap) == "X":
                        Xwins.append(route+r)
                        # print("Xwon",*NewMap,sep="\n")
                        # print("route",Xwins[-1])
                        Flag = True
        if Flag != True:
            for i in range(3):
                for j in range(3):
                    if Map[i][j] == "*":
                        r = []
                        NewMap = Map_Changer(Map, "X", (i, j))
                        r.append((i, j, "X"))
                        Flag = Check_Win(NewMap)
                        if Flag == "Draw":
                            Draws.append(route+r)
                        if Flag != "Draw":
                            for q in range(3):
                                for w in range(3):
                                    if NewMap[q][w] == "*":
                                        r2 = []
                                        NewMap2 = Map_Changer(
                                            NewMap, "O", (q, w))
                                        r2.append((q, w, "O"))
                                        if Check_Win(NewMap2) == "O":
                                            Flag = False
                        if Flag != False and Flag != "Draw":
                            abselotwin = True
                            for q in range(3):
                                for w in range(3):
                                    if NewMap[q][w] == "*":
                                        r2 = []
                                        NewMap2 = Map_Changer(
                                            NewMap, "O", (q, w))
                                        r2.append((q, w, "O"))
                                        a = Think(NewMap2, route+r+r2)
                                        if a == False or a == "Draw":
                                            abselotwin = False
                                            Flag = False

                            if abselotwin:
                                TricWin.append(route+r)

        return Flag

    Think(GameMap)

    # for i in TricWin:
    #     print(*i)
    # print(len(Xwins),len(TricWin),len(Draws))
    # if len(TricWin) !=0:
    #     Map_Changer(GameMap,)
Ai()
# for i in GameMap:
#     print(*i)
