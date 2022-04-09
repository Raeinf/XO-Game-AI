

def x (h=0):
    if h>=2:
        return 0
    for i in range(2):
        print(i,"hello",h)
        h+=1
        x(h)
x()