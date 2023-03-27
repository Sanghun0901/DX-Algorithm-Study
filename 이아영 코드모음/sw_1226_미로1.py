
T = int(input())
for t in range(1, T+1):
    N = int(input())                                           
    arr = [list(map(int, input())) for _ in range(N)]     
    delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]     
    visit = [[False] * N for _ in range(N)]   
    stack = []
    res = 0

    for i in range(N):
        for j in range(N):                
            if arr[i][j] == 2:            
                stack.append((i, j))       

   
    while stack:               
        ix, iy = stack.pop()   
        for x, y in delta:     
            dx = ix + x
            dy = iy + y
            if 0 <= dx < N and 0 <= dy < N:  
                if arr[dx][dy] == 0 and visit[dx][dy] == False:    
                    visit[ix][iy] = True
                    stack.append((dx, dy))  
                elif arr[dx][dy] == 3:
                    res = 1   
                    break



    print(f'#{t} {res}')
