def hinge_loss(x, y, l, a, b, c):
    loss = 0
    for i in range(len(x)):
        loss += max(0, 1 - l[i] * (a * x[i] + b * y[i] + c))
    return loss / len(x)

def dadl(x, y, l, a, b, c):
    gradient = 0
    for i in range(len(x)):
        if l[i] * (a * x[i] + b * y[i] + c) < 1:
            gradient -= l[i] * x[i]
    return gradient / len(x)

def dbdl(x, y, l, a, b, c):
    gradient = 0
    for i in range(len(x)):
        if l[i] * (a * x[i] + b * y[i] + c) < 1:
            gradient -= l[i] * y[i]
    return gradient / len(x)

def dcdl(x, y, l, a, b, c):
    gradient = 0
    for i in range(len(x)):
        if l[i] * (a * x[i] + b * y[i] + c) < 1:
            gradient -= l[i]
    return gradient / len(x)

def normalize_data(x_vals, y_vals, l_vals):
    x_min, x_max = min(x_vals), max(x_vals)
    y_min, y_max = min(y_vals), max(y_vals)
    x_norm, y_norm, l_norm = [], [], []
    for i in range(len(x_vals)):
        x_norm.append((x_vals[i] - x_min) / (x_max - x_min))
        y_norm.append((y_vals[i] - y_min) / (y_max - y_min))
        l_norm.append(l_vals[i])
    return x_norm, y_norm, l_norm, x_min, x_max, y_min, y_max

def adjust_params(a, b, c, x_min, x_max, y_min, y_max):
    a_new = a / (x_max - x_min)
    b_new = b / (y_max - y_min)
    c_new = c - a * (x_min / (x_max - x_min)) - b * (y_min / (y_max - y_min))
    return a_new, b_new, c_new

k = int(input())
x, y, l = [], [], []
for _ in range(k):
    x1, y1, l1 = map(int, input().split())
    x.append(x1)
    y.append(y1)
    l.append(l1)

x, y, l, x_min, x_max, y_min, y_max = normalize_data(x, y, l)

a, b, c = 0.1, 0.0, 0.0
alpha_a, alpha_b, alpha_c = 2.8, 2.8, 2.8

for _ in range(700):
    a -= alpha_a * dadl(x, y, l, a, b, c)
    b -= alpha_b * dbdl(x, y, l, a, b, c)
    c -= alpha_c * dcdl(x, y, l, a, b, c)

a, b, c = adjust_params(a, b, c, x_min, x_max, y_min, y_max)

print(a, b, c)
