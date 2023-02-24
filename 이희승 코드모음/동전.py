a,b = map(int,input().split())
c=[]
count=0
for i in range(a):
    c.append(int(input()))
    c.sort(reverse=True)
for i in range(len(c)):
    if b//c[i] !=0:
        count = count+ b//c[i]
        b=b%c[i]
print(count)
