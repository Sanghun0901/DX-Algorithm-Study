N,L,H= map(int, input().split())
movies= sorted(list(map(int, input().split())))

if L!=0:
    del movies[:L]
if H!=0:
    del movies[-H:]
    
print(sum(movies)/len(movies))
