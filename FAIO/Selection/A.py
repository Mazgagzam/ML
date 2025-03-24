from math import factorial

n, k = int(input()), int(input())
print(int(factorial(n)/(factorial(k)*factorial(n-k))))
