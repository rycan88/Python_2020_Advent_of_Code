
inp = '''Player 1:
4
25
3
11
2
29
41
23
30
21
50
8
1
24
27
10
42
43
38
15
18
13
32
37
34

Player 2:
12
6
36
35
40
47
31
9
46
49
19
16
5
26
39
48
7
44
45
20
17
14
33
28
22'''


L = inp.split("\n\n")

MyDeck = list(map(int,L[0].split("\n")[1:]))
OpDeck = list(map(int,L[1].split("\n")[1:]))


def subfight(D1,D2):
    Found = set()
    #print("YE")
    while True:
        thing = (tuple(D1),tuple(D2))
        if thing in Found:
            return "me"
        else:
            Found.add(thing)
        #print("subgame",thing)
        winner = None
        if 0 in (len(D1), len(D2)):
            break
        if D1[0] <= len(D1) - 1 and D2[0] <= len(D2) - 1:
            winner = subfight(D1[1:1+D1[0]], D2[1:1+D2[0]])

        if D1[0] > D2[0] or winner == "me":
            D1.append(D1.pop(0))
            D1.append(D2.pop(0))
        else:
            D2.append(D2.pop(0))
            D2.append(D1.pop(0))
    if len(D1) != 0:
        return "me"
    return "you"

Found = set()
while True:
    thing = (tuple(MyDeck), tuple(OpDeck))
    if thing in Found:
        break
    else:
        Found.add(thing)
    winner = None
    if 0 in (len(MyDeck),len(OpDeck)):
        break
    if MyDeck[0]<=len(MyDeck)-1 and OpDeck[0]<=len(OpDeck)-1:
        winner = subfight(MyDeck[1:1+MyDeck[0]],OpDeck[1:1+OpDeck[0]])
        #print("oh",thing)
        #print(winner)
        if winner == "me":
            MyDeck.append(MyDeck.pop(0))
            MyDeck.append(OpDeck.pop(0))
        else:
            OpDeck.append(OpDeck.pop(0))
            OpDeck.append(MyDeck.pop(0))
    elif MyDeck[0]>OpDeck[0]:
        MyDeck.append(MyDeck.pop(0))
        MyDeck.append(OpDeck.pop(0))
    else:
        OpDeck.append(OpDeck.pop(0))
        OpDeck.append(MyDeck.pop(0))
    #print(thing)
answer = 0
if len(MyDeck) != 0:
    Deck = MyDeck
else:
    Deck = OpDeck
mult = len(Deck)
for x in Deck:
    answer+= x*mult
    mult-=1
print(answer)



'''
L = inp.split("\n\n")

MyDeck = list(map(int,L[0].split("\n")[1:]))
OpDeck = list(map(int,L[1].split("\n")[1:]))

while True:
    if 0 in (len(MyDeck),len(OpDeck)):
        break
    if MyDeck[0]>OpDeck[0]:
        MyDeck.append(MyDeck.pop(0))
        MyDeck.append(OpDeck.pop(0))
    else:
        OpDeck.append(OpDeck.pop(0))
        OpDeck.append(MyDeck.pop(0))

answer = 0
if len(MyDeck) != 0:
    Deck = MyDeck
else:
    Deck = OpDeck
mult = len(Deck)
for x in Deck:
    answer+= x*mult
    mult-=1
print(answer)
'''