# 전자레인지
n= int(input())
count=[]
arr=[300,60,10] # 시간(분 단위)

if n%10 !=0:
    print(-1)
else:
    for i in arr:
        count.append(n//i) #몫을 리스트에 추가
        n= n%i #나머지를 n으로 변환
    print(*count, sep=' ')     
