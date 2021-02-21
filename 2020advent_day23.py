import time

inp = "792845136"

class Node():
    N = {}
    def __init__(self,num):
        Node.N[num] = self
        self.num = num
        self.next = None

t1 = time.time()
L = list(map(int,list(inp)))
cups = 1000000
L.extend(range(10,cups+1))
current = Node(L[0])

for x in range(1,cups):
    Node.N[L[x-1]].next = Node(L[x])

Node.N[cups].next = current
for turn in range(10000000):
    first = current.next
    second = first.next
    third = second.next
    next = third.next
    picked = (first.num,second.num,third.num)
    current.next = next
    num = current.num
    num-=1
    if num == 0:
        num = cups
    while num in picked:
        num -= 1
        if num == 0:
            num = cups
    new = Node.N[num]
    third.next = new.next
    new.next = first
    current = current.next

one = Node.N[1]
first = one.next
second = first.next
print(first.num,second.num)
print(first.num*second.num)
print(time.time()-t1)


'''
string = inp

for turn in range(100):
    current = string[0]
    picked = string[1:4]
    new = string[4:]
    new += current
    current = str((int(current)-1)%10)
    while current not in new:
        current = str((int(current)-1)%10)
    i = new.index(current)
    New = new[:i+1]
    New += picked
    New += new[i+1:]
    string = New

i = string.index("1")
answer = string[i+1:]+string[:i]
print(answer)
'''
