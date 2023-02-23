n= int(input())
time = sorted(list(map(int, input().split())))
result=0
for i in range(n, 0, -1):
    result+=sum(time[:i])
    
print(result)
