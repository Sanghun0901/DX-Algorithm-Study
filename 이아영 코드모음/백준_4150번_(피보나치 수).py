#피보나치 수
n= int(input())
f=[0,1,1] #리스트의 순서 특성을 잘 사용하기
for i in range(3, n+1):
    f.append(f[i-1]+ f[i-2]) #문제에 힌트가 나와있다. 
print(f[n])
