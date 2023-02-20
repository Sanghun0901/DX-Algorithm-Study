# 대표값
a=[]
for i in range(5):
    n=int(input(""))
    a.append(n)
print(sum(a)//len(a))
print(sorted(a)[2]) # sorted는 리스트 원본 값은 그대로이고 정렬 값을 반환
