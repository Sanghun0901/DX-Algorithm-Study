num = int(input())
max3 = []

for _ in range(num) :
  nums = list(map(int,input().split()))
  nums.sort(reverse = True)
  maxn = nums[2]
  max3.append(maxn)

for i in max3 :
  print(i)
