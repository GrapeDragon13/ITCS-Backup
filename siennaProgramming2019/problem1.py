'''
M = int(input())
N = int(input())
Q, R = M // N
R = M % N
print(M, N, Q, R)
'''

M, N = int(input()), int(input())
print(M, N, M // N, M % N)