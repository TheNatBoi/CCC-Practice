from math import comb
w = input().split(" ")
N = int(w[0])
K = int(w[1])
print(comb(N, 2) - K)