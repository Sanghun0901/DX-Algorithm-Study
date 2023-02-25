a = int(input())
b=list(map(int,input().split()))
b.sort()
count = 0
sum = 0
for i in range(len(b)):
    count =count+ b[i]
    sum = sum+count
print(sum)
