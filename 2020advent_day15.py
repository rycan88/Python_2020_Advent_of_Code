import time


inp = "0,1,5,10,3,12,19"

L = inp.split(",")
L = list(map(int,L))
D = {}
for turn in range(30000000-1):
    if turn<len(L)-1:
        D[L[turn]] = turn
    else:
        if L[turn] in D:
            L.append(turn-D[L[turn]])
            D[L[turn]] = turn
        else:
            L.append(0)
            D[L[turn]] = turn

print(L[-1])


'''
L = inp.split(",")
L = list(map(int,L))
D = {}
for turn in range(2020-1):
    if turn<len(L)-1:
        D[L[turn]] = turn
    else:
        if L[turn] in D:
            L.append(turn-D[L[turn]])
            D[L[turn]] = turn
        else:
            L.append(0)
            D[L[turn]] = turn

print(L[-1])
'''