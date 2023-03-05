# 백준 11721번(열 개씩 끊어 출력하기)
n= str(input())
for i in range(len(n)//10):
    print(n[i*10:i*10+10], sep='\t')
if len(n)%10 !=0:
    print(n[-(len(n)%10):])
