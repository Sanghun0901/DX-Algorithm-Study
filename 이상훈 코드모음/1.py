num = int(input())
shark = list(map(int,input().split()))

def sharkmax(shark):
    dp = [1] * num
    for i in range(num):
        for j in range(i):
            if shark[i] > shark[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


print(sharkmax(shark)) 
