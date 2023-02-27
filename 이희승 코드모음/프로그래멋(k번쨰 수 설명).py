def solution(array, commands):
    answer = []
    for i in commands:
        ary=array[i[0]-1:i[1]]
        ary.sort()
        answer.append(ary[i[2]-1])
    return answer

#answer 리스트 생성
#for 문 사용하여 commands 값으 받은 [2,5,3] 이런식으로 받게됨
#ary 변수 사용하며, array[i[0] -1:i[1]] 이렇게 할시 (2-1):4
#이렇게 받게되서 array 리스트안에있는 5 2 6 3 이 선택 됨
#이것을 sort() 함수 사용하여 정률하면 2 3 5 6이 나오게되며
# [2,5,3] 기준으로 3번째 요소를 가져와야하기 때문에 ary[i[2] -1] 를 해줘 
#2 3 5 6에서 3번째 값인 5를 가져온다 이런식으로 3번을 반복하게 됩니다
