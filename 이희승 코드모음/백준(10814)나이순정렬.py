a = int(input())
c = []
for i in range(a):
    b =list(map(str,input().split()))
    c.append(b)
c.sort(key = lambda x:int(x[0]))
for i in c:
    print(i[0],i[1])
