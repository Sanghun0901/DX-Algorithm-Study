# 우주선 착륙하기 
T= int(input())
delta=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
result=[]
for _ in range(T):
    N,M= map(int, input().split())
    arr=[list(map(int, input().split())) for _ in range(N)]
    final_count=0
    for i in range(N):
        for j in range(M):
            count=0
            for x,y, in delta:
                x1= i+x
                y1= j+y
                if 0<= x1< N and 0 <= y1 <M:
                    if arr[i][j]> arr[x1][y1]:
                        count+=1
            if count>=4:
                final_count+=1
    result.append(final_count)
for k in range(T):
    print('#',k+1, result[k])    
