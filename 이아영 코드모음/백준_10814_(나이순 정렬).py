# 10814번 나이순 정렬

import sys
N= int(sys.stdin.readline())
arr=[]

for i in range(N):
    age, name= map(str, sys.stdin.readline().split())
    arr.append([int(age), name])
               
for j in range(len(arr)):
     
