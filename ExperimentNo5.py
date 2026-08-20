def get_lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    index = dp[m][n]
    lcs_string = [""] * index
    
    i = m
    j = n
    
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return dp[m][n], "".join(lcs_string)

if __name__ == "__main__":
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    
    length, lcs_str = get_lcs(S1, S2)
    
    print(f"String 1: {S1}")
    print(f"String 2: {S2}")
    print("-" * 30)
    print(f"LCS Length: {length}")
    print(f"Longest Common Subsequence: {lcs_str}")
