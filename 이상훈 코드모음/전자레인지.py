num = int(input())
time = [300,60,10]
combo = []

if num%10 != 0 :
    print(-1)
    
else:
    for i in time :
        if num//i > 0 :
            combo.append(num//i)
            num -= i * (num//i)    
        else : 
            combo.append(0)

print(*combo)
