import math

inp = '''......##....#...#..#.#....#....
.......#...#..#..#....##.......
#.#...#........###.#.##..#.....
.......#.....##.#..##...##.##..
.#...#.#...##..........#..#....
#.......##.....###.#...#......#
.........#....#.#.......#..#...
..#.......####.......###..##...
.#.#.##..#.#...##..#...###...##
...................#...........
....#.#.......#..........#.#..#
..#.#...........####.#.......#.
.....#.##..#..##..#.#...#......
#.##...###..#................##
...#...#...#..##.#............#
#.##....##....#........#..#....
..#......#.#.....##.......#....
.......#......#....#......#....
.#........##.....#.#...#...#.#.
..........##.#...#..#..........
#####..##......#.....#......#.#
......#...............##...#...
..#.#.##..#...#.#........#...#.
..........#......#..........###
..#...##.##..##..........#.....
........#.##.#.....#..#...#....
#.....#.........#..............
..........##.##....#..#..#.....
..#...........#.......#........
........#..#.....#.#.#...#.....
#.......##.....#.....#...#.##..
###.#.#....#..#.....#........#.
..#..#..#..........#....#....#.
..#...##...#.#.##.....#..#.....
...#....###...........##.#.....
.##.................##.#.......
........#...#.##..#...#........
.##..#............##..........#
............###.#....#..#......
.....##....#.....#......#.....#
....#.....#.##.......#...#.#...
.##.#......#.........#...##....
..##......#......#...........#.
.......#.#.............#.......
.##.#...#..##....##.......#....
...#......##.#.#......#.....###
#.#....#.......#.#......#....#.
#......#.#.....#...........#..#
##.#..##...#........#.##.#....#
.....#........#........#...#...
...............#.......#..#....
.#.#.#..#.#...#.......#.....##.
.#.#.............#..#....#.....
....#.......#..##.........###..
.#.....#.#....#..#..#....#.....
........#......#.....#.#....#..
##......#....##.....#.#..#.#...
.#...#..#.##.#.##.##.....#.....
#...#....#.........##.#....#...
.........##..#.....#..#...#.#..
.#............#..........#.#...
...........#.....#......#.#....
#...#...#.....#..#....#........
#..##.....#..#.......#....#...#
#..#..#..........#......#...#..
...#...#.#.##.#...#....#...##..
......##....##....#....##..####
...###.#..#....#.......#.......
#.........##......#...#........
..........#....#.......#.......
#....##................##....##
.........#....#.#.......##.#...
.....#......###.......#..#...##
###.....#..##....###...........
.....#...#....#.....##......###
.#..#...#......##........##..#.
#.#.#.#....#.............#.....
......#.....##.#....#..##...#..
..#............#.#....#..#...#.
.............#.#...##.......#..
...#....#.##.#...#.#..##...###.
...#..............#.......#....
......###.#............#.....#.
.##...###..#.####...#..........
...#..#...#.#.#..#......#..#...
.#....##.###....#........#.....
..#..#....#.........##.........
..........##.###........#.#...#
.........#...#..#........#.....
.......#.....#...###...........
.....#.#..##......#...#...#....
.....#....#..#........##.#..#..
...#...........#............#..
##.....#....#.#...#...#....##..
...#.....#.....#...##...#...#..
...##.#..........##...#.#.##.#.
....#.#.##.......#.#...#......#
......###...#....#.##........#.
.....#.........#...#...#..#..##
.........#................#....
.##..###..................#.#.#
.##...........#...........#....
#...#........#.....#..#...##...
.....#..#...#.........#.......#
..#..............#......#......
#....#...............#.#.......
...#........#.#....#..#.###.##.
.......#..##..#...#..#...###...
..........##..#.......##.##....
##.#..#.#...##..........#......
.#.##.#...##.....#....#....#.##
...#.#......#...#.##..##.......
##.......#.#......#....##..#.#.
...#..#.##.........#...#.....#.
.##.##..##...#........#..#.....
.#.##.............#.#.#.....#..
.......#.....................#.
......#...#....#..#..........#.
..#..#....#.#................#.
..#.....#..#.#......#......###.
...#...##..##....#..#...###.#..
...#.....#............##......#
.......#.#.#......#.....###....
.....#......#.....#.........#.#
#...#.#...#..#...#..#....#.....
#..##...#..##.............#..#.
##....##.......#.#.......#..#.#
..............#...#..#......#..
..#...#...#.#...#.#............
#..........#...#.............#.
..........##......#........#...
#...#...#....#.#...........#...
..#.#.#...##......#.#...#.#..#.
.......#.......#.............#.
.#..........#..................
..##...#......#..........#....#
.#..##..........#...#..........
...#....#..#.#.....##..##.#..#.
...#...#...#..#....##..#....#..
..............#.#.....#......##
..............####....#.#..#...
.#........##....#...#.#...#..#.
.#..##.###....#.#.....##..#....
...###.#.........#..#..#.##.#..
.....#..#.....#..#...##......##
.#.#.##.............#...##.....
....##........#........#.......
.......#.....###..............#
#.##.......##....#.#.....#.#...
........#....#............#..##
...#.#..#.......#..........#...
..##....#..##......###.#.....#.
.#..#.#.##....#.......#........
........#.####.#.......#.##....
..........##...............#...
.#..#.....#....##..#..##...#..#
....#.#.....#.#.........#####..
...#.##....#...###.##.#..#.....
.#...........#.............##.#
..#....#....####.....#.#....#..
......##.......#....#..#.......
.####...##.#.#..#.####.#.#.....
###.........#..#.#.#.#........#
...#...#..#.............#.##...
.........#....#......#.....#.#.
...#....#......#..#......#....#
..#...#..........##..##........
.....##........#......#.....#..
...#....#....#....#..#....#....
##...#...........##............
.......#..##..#.......##.#.....
...............#.##.....#......
#.#....##.#.....#...#..........
........#......#...#......#.#.#
..#..#.....#.#........#........
..####.....##.#.##.......#.#.#.
.#.##.#.......##......#.....#..
....#.....##.........#.....#...
.#.#...###.#.#..........#....#.
.........##.#.#.....#..#.......
......#..#...#..#..###.#.#.....
.....#...#.#..#.#.......#.#...#
......##........#..#...#......#
#..##...#...#..#.....#..#..#..#
......#....#...........#.#.....
...#.......#...............#...
#.........#......#.............
..###..................#......#
#.....#.#.#.......##....#......
.........#...........#....#.#..
.###....##.##..##.............#
.##.#......#...#...##..........
....#........###......#.#......
...........#..#.##.#...........
.#..#.......#......#.#####.....
....##....##......#....#...#...
.......#..#.....#.#...###...#.#
..##.....#.......#.#.#..#.....#
.#...#............#....##...#..
.#..#...##.......#.............
..##.......#...........#.#....#
...#.#...#....#..#.....#.......
...#........#...##...#.#..#.#..
#........#..........#..........
......#......#.........#.......
...##...#.....#.......#...#.##.
......##..##......#..###..#....
....##....#..###.#.....##......
##.##..#.....#..#..............
..#.#..#....#....#....#.#...#.#
.#.....##.#.##.#..#.#..........
...#......##.#...##..##...#....
.###.....#......#.......#.....#
....##.......#.....#..#....#...
..........#..##....#..##.#....#
...#....#..##.#........#.#.#...
...#.#...#....#.......#..##.#.#
#..#..........#.#...#....#.....
#..#...........................
........#.....#.....#.#...#.#..
#...#..#...#..........###...#.#
.....##.#..##.#.#.#.##....#....
#.......#....#.#..#..#..#.#....
..###.#.......#.#.##...........
#....#..#..........#.##..#.#...
..#..#........##....#..##......
#...##..#.........#.#....#.#...
##..###..##...#.........#.#...#
###..#....#..##...#.#..#.#.....
.#.##.#......#............#....
.#...#.##.#.........##.........
##.....###.....#........#..#...
...........##.#................
.#......###......#....#..####..
#...##.....#.....#..##....#.#..
..#....#.......#.#.#......#...#
#.....#........#....#.#...#....
..##...............#....#..###.
.#....#.......#..#...#.........
.##.#..#..#...#..#..#....#....#
.......#.#....#.....##...#.....
.#....#.#.#...........#........
.........#..##..#..#...#.......
##..##...#......#.....#........
#...........#.....#..###......#
.#...........#....#...#...##.#.
..............##.###.#.#####.##
........#.#...#.............##.
#...................###..#.##..
#.....#...##...................
.....##..........#..#.#........
.#....##.#....#....###....#...#
.......#.#...........#.#.....#.
......#........###...#...##....
.##..........#..#..#...........
....#.......#..#.....##.#..#...
..#.##......#..#.....#..#......
......#...#..##....#.#..#..#.#.
#.........................#...#
###.#.......#......##....#..#..
..##.###.#...#.............#...
.....#...#...#......#....#####.
#..........#.#.##.#.#.....#..#.
....#.........#...#.#.........#
#.##.........#...#...#.####..##
.##.................#..........
##.....#............#..#.#.....
#.#...#.#........#........#...#
.#...........#....#..#.......#.
.#.......#..........##..#.##..#
.#..##....#..##......#.#..##...
#......#............#.......#.#
.##...............#...#...#....
.......##.#..#..##.....#.......
...#.......#..###.....#....#...
......#............#...........
####............#.........#.##.
#......#.#..#...#.....#..#.....
...........#...#..##.......####
#.#...##..#....#.#.........#.#.
...#....#..#.......#.........#.
.........#.#.#...#....#........
.#.....#........#..#.........#.
....#....#..#.....#...#........
..#....#.#.....#..##...........
.#...#..#..#.##.###....#.......
#......##.......##..##.........
...#.........#.......##.#......
.#...#...#.......#........##...
..#.............#.......#.....#
..#...........#.#.#...#.......#
.....##..#....#..............#.
#.#.....#.#....................
.....#..##..#...#.....#........
..#.......#..####..#....#.##.#.
#....#.....#.....#...#......#..
..#....##...#....#..#..#.....#.
..#.####..............##.......
.#.........#..#...#.......##...
#....#.#........#....#...#...##
.....#..#....#.#..#...#.#.##...
.##.................#...##.....
.##.##.##...#...........#...##.
..#....#..#.....#..#......##...
.#...........#......#....#..#.#
.#.#............#..#..#...#....
....#......#.....#.#.#.....#...
#.......##.............#.......
....#....................#.#...
......#........#..#.#.....#.#..
.....#..#....#.#........#....#.
...##.........#...#.##....#..#.
.#....#..#...#.#.#......#......
#......#.#.##.#..#..#.....##...
......#....#.#...#..#.#........
..#.....##.....#...#.#.......#.
......#.#.....#........#.......
......#.#.#...#..#.#.#.#.......
..#.#.##..#..#..#.#.##...#.....
......#.#.#......#.....#...#...
.....#.##....#..##...#...#....#
..#.....#...........#..#..##...
..#..#.......#....#....###.#...'''



L = inp.split("\n")
rowlength = len(L[0])
def foo(right,down):
    count = 0
    for y in range(1,math.ceil(len(L)/down)):
        if L[y*down][(right*y)%rowlength] == "#":
            count+=1
    return count
print(foo(3,1)*foo(1,1)*foo(5,1)*foo(7,1)*foo(1,2))


'''
L = inp.split("\n")
rowlength = len(L[0])
count = 0
for y in range(1,len(L)):
    if L[y][(3*y)%rowlength] == "#":
        count+=1

print(count)
'''

