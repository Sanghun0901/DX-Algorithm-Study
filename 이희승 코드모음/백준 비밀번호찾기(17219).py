a = int(input())
sum = 0
sum1 = 0
b= list(map(int,input().split()))
c= list(map(int,input().split()))
b.sort()
c.sort(reverse=True)
for i in range(a):
    sum = b[i]*c[i]
    sum1 = sum+sum1
print(sum1)
