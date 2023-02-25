a = int(input())
for i in range(a):
    c=list(map(int,input().split()))
    c.sort()
    c.pop(0)
    c.pop(-1)
    if max(c) - min(c)<4:
        print(sum(c))
    else:
        print('KIN')   
