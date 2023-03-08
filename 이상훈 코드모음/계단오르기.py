num = int(input())
if num == 0:
    print(0)
else:
    stair = []
    stair.append(0)
    for _ in range(num):
        a = int(input())
        stair.append(a)
    
    d = [0]*(num+1)
    if num == 1:
        d[1] = stair[1] # 1번계단
    elif num == 2:
        d[1] = stair[1] # 1번계단
        d[2] = d[1] + stair[2] # 1번계단을 밣은 후 2번계단 선택
    elif num == 3:
        d[1] = stair[1] # 1번계단
        d[2] = d[1] + stair[2] # 1번계단을 밣은 후 2번계단 선택
        d[3] = max(d[1]+ stair[3],stair[2]+stair[3]) # 계단이 3개까지만 있을 때의 메모제이션 4개일때 0 1 2 3 4 -> (1,2,4) (1.3.4) d[2] st4 , d[1],st3

    else :
        d[1] = stair[1] # 1번계단
        d[2] = d[1] + stair[2] # 1번계단을 밣은 후 2번계단 선택
        d[3] = max(d[1]+ stair[3],stair[2]+stair[3]) # 계단이 3개까지만 있을 때의 메모제이션 4개일때 0 1 2 3 4 -> (1,2,4) (1.3.4) d[2] st4 , d[1],st3

        for i in range(4,num+1) : #계단이 4부터 num까지 존재할 때의 메모제이션 5까지일때 -> 0 1 2 3 4 5 (1,2,4,5) (1,3,5)
                d[i] = max(d[i-2]+ stair[i], d[i-3]+stair[i-1]+stair[i]) # d[3] st5 , d[2] st4
            

    print(d[num]) 
