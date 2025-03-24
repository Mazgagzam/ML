a, b, c = map(int, input().split())

mt1 = []
mt2 = []
mt3 = [[0] * c for _ in range(a)]

for _ in range(a):
    mt1.append(list(map(int, input().split())))

for _ in range(b):
    mt2.append(list(map(int, input().split())))

for i in range(a):
    for j in range(c):
        for l in range(b):
            mt3[i][j] += mt1[i][l] * mt2[l][j]
        if mt3[i][j] <= 0:
            print("found 0")
            break
    else:
        continue
    break
else:
    for row in mt3:
        print(*row)
