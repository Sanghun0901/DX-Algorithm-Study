num = int(input())
chaek = []
for _ in range(num) :
  cnt = 0
  chance = int(input())
  c1 = list(map(str,input().split()))
  c2 = list(map(str,input().split()))
  c1.sort()
  c2.sort()
  for i in range(chance) :
    if c1[i] != c2[i] :
      cnt += 1
    else : pass
  chaek.append(cnt)

for i in chaek :
  if i > 0 :
    print('CHEATER') 
  else :
    print('NOT CHEATER') 
