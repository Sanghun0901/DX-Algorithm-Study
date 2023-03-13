# 1789번 수들의 합
n= int(input())
sum=0
s=0
for i in range(1,n+1):
    sum+=i
    s=i
    if sum > n:
        s-=1
        break
print(s)
