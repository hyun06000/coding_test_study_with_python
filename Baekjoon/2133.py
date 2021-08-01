N = int(input())

if N % 2:
    print(0)
else:
    N = N//2
    dp = [3, 11]
    if N <= 2:
        print(dp[N-1])
    else:
        for i in range(1, N-1):
            dp.append(3 * dp[i] + sum(dp[0:i]) * 2 + 2)
        print(dp[-1])
