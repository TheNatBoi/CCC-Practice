o = "#"
t = """.#.
###
.#."""
f = """..#..
.###.
#####
.###.
..#.."""
s = """...#...
..###..
.#####.
#######
.#####.
..###..
...#..."""
for _ in range(5):
    d = int(input())
    if d == 1:
        print(o)
    elif d == 3:
        print(t)
    elif d == 5:
        print(f)
    elif d == 7:
        print(s)