a = int(input())
for i in range(a):
    b=list(map(int,input().split()))
    b.sort()
    b.sort(reverse=True)
    print(b[2]) 
