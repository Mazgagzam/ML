from statistics import quantiles


data = list(map(float, input().split()))
data1 = sorted(data)

q1 = quantiles(data1, n=100)[24]
q3 = quantiles(data1, n=100)[74]
iqr = q3 - q1
low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr
print(*[x for x in data if x < low or x > high])
