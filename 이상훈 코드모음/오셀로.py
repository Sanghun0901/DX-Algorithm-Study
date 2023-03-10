num = int(input()) # 게임 수행 횟수
result = []
for _ in range(num) :
    game = int(input()) # 오셀로 한줄의 개수
    R1 = list(input())
    R2 = list(input())
    cnt = 0
    BW = 0
    WB = 0
    for i in range(game) :
        if R1[i] == 'B' and R2[i] == 'W' :
            BW += 1
            cnt +=1
        elif R1[i] == 'W' and R2[i] == 'B' : 
            WB += 1
            cnt +=1
    
    while BW !=0 and WB != 0 :
        BW -= 1
        WB -= 1
        cnt -= 1
        
    result.append(cnt)

for i in result :
    print(i)
