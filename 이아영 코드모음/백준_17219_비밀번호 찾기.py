# 17219번 비밀번호 찾기
import sys
n, m = map(int, sys.stdin.readline().split())
arr=[]
id=[]
for i in range(n+m):
    if i<n:
        arr.append(list(map(str, sys.stdin.readline().split())))
    else:
        id.append(str(sys.stdin.readline().rstrip()))
password= [arr[b][1] for a in range(m) for b in range(n) if id[a]==arr[b][0]]
print(*password, sep='\n')
