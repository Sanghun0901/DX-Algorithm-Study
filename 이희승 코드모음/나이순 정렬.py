a = int(input())                                 #a변수값을 받고 입력
c = []                                           #c변수 리스트 생성을 한후
for i in range(a):                               #for 문을 이용하여 리스트를 입력받고 그 입력받은 리스틀를
    b =list(map(str,input().split()))            #c리스트에 추가     
    c.append(b)                                  # 그후 sort()함수를 이용하여 숫자들끼리만 정렬 
c.sort(key = lambda x:int(x[0]))                 # 정렬된 숫자만 문자를 차례로 print 사용해서 꺼내옴
for i in c:
    print(i[0],i[1])
