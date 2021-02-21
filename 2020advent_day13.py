
inp = '''1000390
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,503,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37'''


def change(num1,num2,q):
    return num2,num1-num2*q


I = inp.split("\n")

L = I[1].split(",")

D = {}
for x in range(len(L)):
    if L[x]!="x":
        num = int(L[x])
        D[num] = x
print(D)

first = True
for i in D:
    print(i)
    if first:
        mod1 = i
        num1 = -D[i]
        first = False
        continue
    mod2 = i
    num2 = -D[i]
    diff = num2-num1
    bignum = mod1 * mod2
    if mod1>mod2:
        x1,r1 = 1,mod1
        x2,r2 = 0,mod2
    else:
        x1,r1 = 0,mod2
        x2,r2 = 1,mod1
    while True:
        q = r1//r2
        r1,r2 = change(r1,r2,q)
        x1,x2 = change(x1,x2,q)
        if r2 == 1:
            answer = (x2*diff*mod1+num1)%bignum
            break
    mod1,num1 = bignum,answer

print(answer)





'''
I = inp.split("\n")
start = int(I[0])
L = I[1].split(",")

lowest = 100000
ID = None
for x in L:
    if x =="x":
        continue

    num = int(x)
    diff = ((start//num)+1)*num-start
    if diff<lowest:
        lowest = diff
        ID = num

print(ID*lowest)
'''