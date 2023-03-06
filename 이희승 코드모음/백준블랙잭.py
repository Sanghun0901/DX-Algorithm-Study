a, b = map(int,input().split())
c =list(map(int,input().split()))
list1=[]
result = 0
for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            if c[i]+c[j]+c[k] > b:
                continue
            else:
                list1.append(c[i]+c[j]+c[k])
print(max(list1))
