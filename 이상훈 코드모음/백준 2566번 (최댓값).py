max_t = []
numbers = []
for i in range(9) :
  nums = list(map(int,input().split()))
  max_t.append(max(nums))
  numbers.append(nums.index(max(nums)))
b = max(max_t)

print(b)
print(max_t.index(b)+1, numbers[max_t.index(b)]+1)
