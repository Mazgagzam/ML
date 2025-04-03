from math import log

def sm_1(m, t, n):
    s = 0
    for i in range(n):
        s += t[i] * log(m[i])

    return s

n = int(input())
m = []
t = []
for _ in range(n):
    m1, t1 = map(float, input().split())
    m.append(m1)
    t.append(t1)

lgm = sum(log(m[i]) for i in range(n))
smt = sum(t)
k = (n * sm_1(m, t, n) - sum(t) * lgm) / (n * sum(t[i]**2 for i in range(n)) - smt**2)

b = (lgm - k*smt) / n

k = abs(k)


T = k**(-1) * log(2)
print(T)
