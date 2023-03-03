a = int(input())
for i in range(a):
    
    b=int(input())
    c=list(map(str,input().split()))
    d=list(map(str,input().split()))
    c.sort()
    d.sort()
    if c==d:
        print('NOT CHEATER')
    else:
        print('CHEATER')
