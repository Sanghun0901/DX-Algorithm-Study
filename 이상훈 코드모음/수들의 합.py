num = int(input())
if num == 1:
    print(1)
if num == 2 :
    print(1)
else :
    for i in range(1,num) :
        num -= i
        if num < 0 :
            print(i-1)
            break
        elif num == 0 :
            print(i)
            break
            
        else : pass
