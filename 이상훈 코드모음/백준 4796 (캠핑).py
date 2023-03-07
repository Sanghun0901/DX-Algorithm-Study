vac = []

while True :
    a = list(map(int,input().split())) #L,P,V 
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    else :
        vac.append(a)
    

for i in range(len(vac)) : 
    if vac[i][2] % vac[i][1] <= vac[i][0]:
        print(f"Case {i+1}: {(vac[i][2]//vac[i][1])*vac[i][0]+vac[i][2]%vac[i][1]}")
    else:
        print(f"Case {i+1}: {(vac[i][2]//vac[i][1])*vac[i][0]+vac[i][0]}")   
