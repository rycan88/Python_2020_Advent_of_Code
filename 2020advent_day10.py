

inp = '''152
18
146
22
28
133
114
67
19
37
66
14
90
163
26
149
71
106
46
143
145
12
151
105
58
130
93
49
74
83
129
122
63
134
86
136
166
169
159
3
178
88
103
97
110
53
125
128
9
15
78
1
50
87
56
89
60
139
113
43
36
118
170
96
135
23
144
153
150
142
95
180
35
179
80
13
115
2
171
32
70
6
72
119
29
79
27
47
107
73
162
172
57
40
48
100
64
59
175
104
156
94
77
65'''



L = list(map(int,inp.split("\n")))
L.append(0)
L.sort()
L.append(L[-1]+3)
D = {}
for x in L:
    D[x] = 0
D[0] = 1

for number in L:
    for x in range(1,4):
        if number+x in D:
            D[number+x]+=D[number]

print(D[L[-1]])


'''
L = list(map(int,inp.split("\n")))
L.append(0)
L.sort()
L.append(L[-1]+3)
one = 0
three = 0
for x in range(len(L)-1):
    if L[x+1]-L[x] == 1:
        one+=1
    if L[x+1]-L[x] == 3:
        three += 1

print(one*three)
'''