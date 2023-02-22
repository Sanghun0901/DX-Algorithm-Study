a,b = map(int,input().split())
r = map(int,input().split())
  
d = list(r)        
d.sort(reverse = True)
         
print(d[b-1])
