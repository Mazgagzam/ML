def solve():
    m = int(input())
    
    words = []
    for _ in range(m):
        words.append(input())
    
    for i in range(m - 2):
        if "Жаңа" in words[i] or "жыл" in words[i]:
            print(2, end=" ")
            return
        
        if words[i][-2:] == words[i + 1][-2:]:
            print(1, end=" ")
            return
        
        if words[i][-2:] == words[i + 2][-2:]:
            print(1, end=" ")
            return
    
    print(2, end=" ")
    
    
n = int(input())
for _ in range(n):
    solve() 
