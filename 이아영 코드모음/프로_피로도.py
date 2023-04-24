# permutations= 순열, 서로 다른 n개의 원소에서 r개를 중복없이 순서 상관있게 선택
from itertools import permutations 

def solution(k, dungeons):
    # 최대 던전 수
    max_count=0
    
    for p in list(permutations(dungeons, len(dungeons))):
        hp= k # 기존 k 값을 보존하기 위해서 
        count=0
        
        for minimum, consume  in p:
            if hp < minimum: # 최소 필요 피로도가 현재 피로도보다 높으면 안된다. 
                break
            else:
                hp-=consume
                count+=1
        if count > max_count:
            max_count= count
    return max_count
            
            
