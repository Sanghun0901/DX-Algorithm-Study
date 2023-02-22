# 커트라인
#map의 기능은 입력받은 수를 공백을 기준으로 분리한 후, 정수형(int)으로 변환시켜 변수에 1:1로 지정해준다. 
n,k= map(int, input().split())
score= list(map(int, input().split()))
score.sort(reverse=True) # sort는 리스트 원본값을 직접 수정. 리턴값이 없다.
print(score[k-1])
