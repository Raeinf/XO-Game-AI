
import sys
print(sys.setrecursionlimit(40000))




GameMap=[ ["*", "*", "*"]
         ,["*", "*","*"]
         ,["*", "*", "*"]]


def Map_Changer(Map,Turn,po):
    m=[]
    for i in Map:
        m.append(i.copy())
    m[po[0]][po[1]]=Turn
    return m


def Check_Win(GameMap):
    for i in range(3):
        if GameMap[i][0] == GameMap[i][1] == GameMap[i][2]:
            return GameMap[i][0]
        if GameMap[0][i] == GameMap[1][i] == GameMap[2][i]:
            return GameMap[0][i]
    if GameMap[2][0]== GameMap[1][1] == GameMap[0][2] or GameMap[2][2]==GameMap[1][1]==GameMap[0][0]:
        return GameMap[1][1]
    draw=0
    for i in GameMap:
        for j in i:
            if j != "*":
                draw+=1
    if draw==9:
        return "Draw"
    

def Ai():
    global GameMap
    Xwins=[]
    Owins=[]
    Draw=[]
    def Think(Map=GameMap,Xturn=True,TempState=[]): # here it will calculate all the conditanos..!
        # there is is little bug here..!
        for i in range(3):
            for j in range(3):
                if Map[i][j] =="*":
                    if Xturn:
                        turn="X"
                    else:
                        turn="O"
                    NewMap=Map_Changer(Map,turn,(i,j))
                    TempState.append((i,j))
                    if Check_Win(NewMap)=="X":
                        Xwins.append(TempState)
                    elif Check_Win(NewMap)=="O":
                        Owins.append(TempState)
                    elif Check_Win(NewMap)=="Draw":
                        Draw.append(TempState)
                    else:
                        Think(NewMap,not(Xturn),TempState)
    Think()

    print(*Xwins[0])
Ai()
# for i in GameMap:
#     print(*i)