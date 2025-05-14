A = int(input())
B = int(input())
N = int(input())
output = list()
output.append(str(A))
output.append(str(B))
dash1 = B
dash2 = A

for i in range(N-2):
    temp = dash1 + dash2
    output.append(str(temp))
    dash2 = dash1
    dash1 = temp
print(','.join(output))