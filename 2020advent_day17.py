
inp ='''##..####
.###....
#.###.##
#....#..
...#..#.
#.#...##
..#.#.#.
.##...#.'''

def add(tup,tup2):
    return (tup[0]+tup2[0],tup[1]+tup2[1],tup[2]+tup2[2],tup[3]+tup2[3])

L = inp.split("\n")

Around = set()
for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            for w in range(-1,2):
                Around.add((x,y,z,w))

Active = set()
for y in range(len(L)):
    for x in range(len(L[0])):
        thing = L[y][x]
        if thing == "#":
            Active.add((x,y,0,0))

for turns in range(6):
    Check = set()
    NewActive = set()
    for active in Active:
        for around in Around:
            Check.add(add(around,active))
    for tup in Check:
        if tup in Active:
            count = 0
            for around in Around:
                if around == (0,0,0,0):
                    continue
                newtup = add(around,tup)
                if newtup in Active:
                    count+=1
                    if count>3:
                        break
            if count in (2,3):
                NewActive.add(tup)
        else:
            count = 0
            for around in Around:
                if around == (0,0,0,0):
                    continue
                newtup = add(around,tup)
                if newtup in Active:
                    count+=1
                    if count>3:
                        break
            if count==3:
                NewActive.add(tup)
    Active = NewActive
print(len(Active))

'''
def add(tup,tup2):
    return (tup[0]+tup2[0],tup[1]+tup2[1],tup[2]+tup2[2])

L = inp.split("\n")

Around = set()
for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            Around.add((x,y,z))

Active = set()
for y in range(len(L)):
    for x in range(len(L[0])):
        thing = L[y][x]
        if thing == "#":
            Active.add((x,y,0))

for turns in range(6):
    Check = set()
    NewActive = set()
    for active in Active:
        for around in Around:
            Check.add(add(around,active))
    for tup in Check:
        if tup in Active:
            count = 0
            for around in Around:
                if around == (0,0,0):
                    continue
                newtup = add(around,tup)
                if newtup in Active:
                    count+=1
                    if count>3:
                        break
            if count in (2,3):
                NewActive.add(tup)
        else:
            count = 0
            for around in Around:
                if around == (0,0,0):
                    continue
                newtup = add(around,tup)
                if newtup in Active:
                    count+=1
                    if count>3:
                        break
            if count==3:
                NewActive.add(tup)
    Active = NewActive
print(len(Active))
'''






