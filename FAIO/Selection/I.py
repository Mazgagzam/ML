def check(x, y, k, b):
    ysh = k * x + b

    return abs(ysh - y)/abs(ysh) >= 0.4

n = int(input())
ind = []
x = []
y = []

for i in range(n):
    ind1, x1, y1, z = map(float, input().split())
    ind.append(ind1)
    x.append(x1)
    y.append(y1)

k = (n *  sum(x1 * y1 for x1, y1 in zip(x, y)) - sum(x) * sum(y)) / (n * sum(x1 ** 2 for x1 in x) - sum(x) ** 2)
b = (sum(y) - k * sum(x)) / n

ans = []
for i in range(n):
    if check(x[i], y[i], k, b):
        ans.append(int(ind[i]))

print(*ans)
