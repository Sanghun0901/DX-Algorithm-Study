num = str(input())
a= list(num)
nums = [10,21,32,43,54,65,76,87,98]
for i in range(1,(len(a)//10)+1):
  a.insert(nums[i-1],' ')

b= ('').join(a)
b = b.split()

for i in b :
  print(i)
