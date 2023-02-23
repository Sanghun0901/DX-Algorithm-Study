# k번째 수 (프로그래머스)
def solution(array, commands):
    answer=[]
    for i in range(len(commands)):
        c= commands[i]
        l, m, n= c[0],c[1],c[2]
        array2= sorted(array[l-1:m])
        answer.append(array2[n-1])
    return answer
