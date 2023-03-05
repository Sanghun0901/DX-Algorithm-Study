a = [] 
max = -1
b=0
c=0
for i in range(9):
    a.append(list(map(int,input().split())))
for i in range(9):
    for j in range(9):
        if a[i][j] > max:
            max = a[i][j]
            b=i+1
            c=j+1
print(max)
print(b,c)
