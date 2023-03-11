import sys 
input = sys.stdin.readline
a = int(input())
sum = 0
cnt =0
for i in range(1,a+1):
    sum=sum+i
    cnt=cnt +1 
    if sum> a:
        cnt = cnt -1
        break
print(cnt)
