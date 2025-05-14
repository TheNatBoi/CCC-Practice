def min_cost_path():
    import sys
    # Read input from standard input
    R = int(sys.stdin.readline())  # Number of rows
    C = int(sys.stdin.readline())  # Number of columns
    M = int(sys.stdin.readline())  # Maximum cost of a tile

    # Function to compute the cost of a tile at (i, k)
    def cost(i, j):
        return ((i-1) * C + (j-1)) % M + 1

    # Initialize the DP table
    dp = [[float('inf')] * (C + 2) for _ in range(R + 1)]

    # Base case: bottom row
    for j in range(1, C + 1):
        dp[R][j] = cost(R, j)

    # Fill the DP table upward
    for i in range(R - 1, 0, -1):  # From row R-1 to row 1
        for j in range(1, C + 1):
            dp[i][j] = cost(i, j) + min(dp[i+1][j-1], dp[i+1][j], dp[i+1][j+1])

    # Find the minimum cost in the first row
    min_cost = min(dp[1][j] for j in range(1, C + 1))

    # Write the result to standard output
    print(min_cost)

# Call the function
min_cost_path()