x1, y1, x2, y2, x3, y3 = map(float, input().split())

t = y2/(x1-x2-x3) - (y3-y1)/(x3-x1)
a = -t/x2
b = (y3-y1) / (x3 - x1) + t*(x3 + x1)/x2
c = y1 + (t*x1**2)/x2-b*x1
print(a, b, c)
