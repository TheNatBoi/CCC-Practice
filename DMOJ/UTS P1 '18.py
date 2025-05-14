T = list(input().split(' '))
M = int(T[0])
N = int(T[1])

print(max(abs(M-N), M+N, M*N))