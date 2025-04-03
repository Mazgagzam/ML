from math import sqrt

def f(x, y, x1, y1):
    return (x - x1)**2 + (y - y1)**2

def aver(n, l):
    return sum(l)/n

def get_t(x, y, k, cx, cy):
    ind = 0
    ras = f(x, y, cx[0], cy[0])
    
    for i in range(1, k):
        ras1 = f(x, y, cx[i], cy[i])
        if ras1 < ras:
          # print(ras1, ras, x, y, cx[i], cx[i])
            ind = i
            ras = ras1

    return ind


n = int(input())
x = []
y = []   

for _ in range(n):
    x1, y1 = map(float, input().split())
    x.append(x1)
    y.append(y1)

k = int(input())

cx = []
cy = []

for i in range(k):
    cx1, cy1 = map(float, input().split())
    cx.append(cx1)
    cy.append(cy1)


for _ in range(500):
    cx1 = [list() for _ in range(k)]
    cy1 = [list() for _ in range(k)]

    for x1, y1 in zip(x, y):
        ind = get_t(x1,y1, k, cx, cy)
        cx1[ind].append(x1)
        cy1[ind].append(y1)

    for i in range(k):
        if len(cx1[i]) <= 0:
            continue
        
        cx[i] = aver(len(cx1[i]), cx1[i])
        cy[i] = aver(len(cy1[i]), cy1[i])




for i in range(k):
    print(cx[i], cy[i])
