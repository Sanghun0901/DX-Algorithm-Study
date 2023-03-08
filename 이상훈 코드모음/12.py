n, m = map(int, input().split())

# 학생이 좋아하는 수를 저장하는 2차원 리스트
grid = [list(map(int, input().split())) for _ in range(n)]

# 최대 정사각형 넓이
max_area = 0

# 모든 정사각형을 순회하면서 최대 정사각형 넓이 계산
for i in range(n):
    for j in range(m):
        # 현재 위치의 학생이 좋아하는 수
        num = grid[i][j]
        
        # 오른쪽, 아래쪽, 대각선 아래 방향으로 선생님이 만든 정사각형이 있는지 확인
        for k in range(1, min(n-i, m-j)):
            # 현재 위치로부터 오른쪽, 아래쪽, 대각선 아래 방향의 학생들의 좋아하는 수
            num_right = grid[i][j+k]
            num_down = grid[i+k][j]
            num_diag = grid[i+k][j+k]
            
            # 만약 네 학생이 서로 같은 수를 좋아하면 정사각형을 만들 수 있음
            if num == num_right == num_down == num_diag:
                # 현재 정사각형의 넓이
                area = (k+1) ** 2
                
                # 최대 정사각형 넓이 업데이트
                max_area = max(max_area, area)

print(max_area)
