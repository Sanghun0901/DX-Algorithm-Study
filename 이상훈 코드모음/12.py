n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

max_area = 0

for i in range(n):
    for j in range(m):
        num = grid[i][j]
        
        for k in range(1, min(n-i, m-j)):
            num_right = grid[i][j+k]
            num_down = grid[i+k][j]
            num_diag = grid[i+k][j+k]
            
            if num == num_right == num_down == num_diag:
                area = (k+1) ** 2
                
                max_area = max(max_area, area)

print(max_area)
