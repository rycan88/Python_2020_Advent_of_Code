
inp = '''6929599
2448427'''

L = inp.split("\n")

num = 1
key = int(L[0])
turns = 0
subjectnum = 7
while True:
    turns+=1
    num*=subjectnum
    num%=20201227
    if num ==key:
        break


num = 1
subjectnum = int(L[1])
for x in range(turns):
    turns+=1
    num*=subjectnum
    num%=20201227
print(num)