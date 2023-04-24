N= int(input())
arr = list(map(int, input().split()))
result= [0] * N

# 반복문을 통해 각 자리에 들어갈 사람 한명씩 확인(키 작은 사람부터)
for i in range(N):
    cnt= 0 # 자신의 왼쪽에 키 큰 사람의 수
            # 각자 왼쪽에 있는 사람의 수가 다르기 때문에 for문 속에 증가시키면서 그 수를 맞춘다
   
    # 한명씩 들어갈 자리 물색하는 과정
    for j in range(N):
        
        if cnt== arr[i] and result[j]==0:
            result[j]= i+1
            break
            
        elif result[j]==0:
            cnt+=1
print(*result)
