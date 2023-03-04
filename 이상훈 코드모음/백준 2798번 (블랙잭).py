card,target = map(int,input().split())
bj = list(map(int,input().split()))
totaltt = []

for i in range(card-2) :
  for j in range(i+1,card-1) :
    for s in range(j+1,card) :
      total = bj[i] + bj[j] + bj[s]
      if total <= target :
        totaltt.append(total)

print(max(totaltt))
