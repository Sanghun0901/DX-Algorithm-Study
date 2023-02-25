a,b,c=map(int,input().split())
d = list(map(int,input().split()))
d.sort()
for i in range(b):
    d.pop(0)
for j in range(c):
    d.pop(-1)
print(sum(d)/len(d))
