# 23968 알고리즘 수업- 버블 정렬1 (파이참으로 해야 시간 오류 벗어낫 수 있다고 함.)
import sys
N,K = map(int, sys.stdin.readline().split())
arr= list(map(int, sys.stdin.readline().split()))
count=0

for i in range(N-1,0,-1):
    for j in range(i):
        if arr[j]> arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count+=1
            
            if count== K:
                print(arr[j], arr[j+1])

if count < K:
    print(-1)
