# 9076 점수 집계
score=[]
n= int(input())
for i in range(n):
    score.append(list(map(int, input().split())))
    
for i in range(len(score)):
    s= score[i] 
    s= sorted(s) # 이 부분 조심하심하기!!
    if s[3]-s[1]>= 4:
        print("KIN")
    else:
        print(s[1]+s[2]+s[3])
