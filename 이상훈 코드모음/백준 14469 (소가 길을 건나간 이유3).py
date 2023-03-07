num = int(input())

time = []
for i in range(num) :
    a = list(map(int,input().split()))
    time.append(a)
    
time.sort(key=lambda x: x[0])

cnt = 0

for i in range(num) :
    if time[i][0] > cnt :
        cnt = time[i][0]
        cnt += time[i][1]
        
    else :
        cnt += time[i][1]
        
print(cnt)
