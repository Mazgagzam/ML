n = int(input())
a = round(((n-1)*(n-2)*(n-3))/(n**3), 2)
b = round(((1*2*3)/(n**3)), 2)
c = round(1 - a, 2)

print(a, b, c)
