# 난쟁이 문제
dwarf =[]               
for _ in range(9):      
    dwarf.append(int(input()))  
for i in range(len(dwarf)):
    for j in range(i+1, 9):
        if sum(dwarf)- (dwarf[i]+dwarf[j]) ==100:
            f1,f2= i,j
            break
dwarf.pop(f1)
dwarf.pop(f2-1)   
dwarf.sort(reverse= False)  
print(*dwarf, sep='\n')   
