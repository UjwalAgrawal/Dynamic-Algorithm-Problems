if __name__ == '__main__':
    x = input("Enter first string: ")
    y = input("Enter second string: ")

    m = len(x)
    n = len(y)

    dp = [[None] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0
    

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[m][n])