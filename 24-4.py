N = int(input())
R = 0
T = 1
while N > 0:
    d = N % 10
    if d != 1:
        R = R + d*T
        T = T + 1
    N = N // 10
print(T)
