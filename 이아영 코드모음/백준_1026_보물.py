# 1026번. 보물
n= int(input())
a= sorted(list(map(int, input().split())))
b= list(map(int, input().split()))
sum=0
for i in range(n):
    sum += a[i]*max(b) 
    del b[b.index(max(b))] --> #리스트에서 요소를 삭제하기 위해서는 인덱스 번호 필요
print(sum)
