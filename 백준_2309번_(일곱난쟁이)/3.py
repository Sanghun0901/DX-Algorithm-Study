b = []
for i in range(9):
     b.append(int(input()))
for i in range(len(b)):
     for j in range(i+1,len(b)):
          if sum(b) - (b[i]+b[j]) == 100:
               x,y=i,j
               break
b.pop(x)
b.pop(y-1)
b.sort()
for i in range(len(b)):
     print(b[i])
