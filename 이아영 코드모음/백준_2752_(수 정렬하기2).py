# 2751 수 정렬하기2, 버블정렬 이용.
n= int(input())
arr=[]
for _ in range(n):
    arr.append(int(input())) #수를 받아서 정렬에 추가
for i in range(len(arr)-1, 0, -1): #거꾸로 
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print(*arr, sep='\n')
