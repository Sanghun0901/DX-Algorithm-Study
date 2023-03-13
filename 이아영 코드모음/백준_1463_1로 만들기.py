# 1로 만들기
d=[0]*(10**6+1)
x= int(input())

for i in range(2, x+1):
    d[i]= d[i-1]+1
    if i%3==0:
        d[i]= min(d[i], d[i//3]+1)
    if i%2==0: # elif 사용하면 속도 느려짐.
        d[i]= min(d[i], d[i//2]+1)
print(d[x])
