n = int(input())

pts = []
for _ in range(n):
    pt = input().split()
    x, y, s = map(float, pt[:3])
    pts.append((x, y, int(s)))

m = int(input())
res = []
for _ in range(m):
    x, y = map(float, input().split())
    min_d = float('inf')
    cnd = []
    for sx, sy, ss in pts:
        d = (x - sx)**2 + (y - sy)**2
        if d < min_d:
            min_d = d
            cnd = [ss]
        elif d == min_d:
            cnd.append(ss)
            
    cnt0 = cnd.count(0)
    cnt1 = len(cnd) - cnt0
    print('0' if cnt0 >= cnt1 else '1', end=" ")
