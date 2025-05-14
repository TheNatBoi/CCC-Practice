grid = []
row = []
r = int(input())
dots = 1
spaces = 2 * r - 2
for _ in range(round(r/2-0.5)):
    row.append("*" * dots)
    row.append(" " * spaces)
    row.append("*" * dots)
    dots += 2
    spaces -= 4
    print("".join(row))
    row = []
print("*" * (2 * r))
dots = r - 2
spaces = 2 * r - 2 * dots
for _ in range(round(r/2-0.5)):
    row.append("*" * dots)
    row.append(" " * spaces)
    row.append("*" * dots)
    dots -= 2
    spaces += 4
    print("".join(row))
    row = []