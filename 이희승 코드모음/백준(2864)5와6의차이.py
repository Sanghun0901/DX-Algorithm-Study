import sys 
input = sys.stdin.readline
a,b =input().split()
max_value = int(a.replace('5','6'))+int(b.replace('5','6'))
min_value = int(b.replace('6','5')) +int(a.replace('6','5'))
print(min_value,max_value)
