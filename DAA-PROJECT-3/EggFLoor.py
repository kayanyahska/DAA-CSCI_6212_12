def eggDrop(m, n):
    # Create a 2D array to store results
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Base cases
    for i in range(1, m + 1):
        dp[i][0] = 0  # 0 floors require 0 drops
        dp[i][1] = 1  # 1 floor requires 1 drop

    for j in range(1, n + 1):
        dp[1][j] = j  # 1 egg requires j drops for j floors

    # Fill the rest of the table
    for i in range(2, m + 1):  # For each number of eggs
        x = 1  # Start from the first floor
        for j in range(2, n + 1):  # For each number of floors
            # Move the floor to drop the egg from
            while x < j and dp[i - 1][x - 1] < dp[i][j - x]:
                x += 1  # Increment x until we find the optimal floor
            # Calculate the minimum drops needed
            dp[i][j] = 1 + max(dp[i - 1][x - 1], dp[i][j - x])

    return dp[m][n]

# Example usage
m = 300  # Number of eggs
n = 14000  # Number of floors
result = eggDrop(m, n)
print(f"Minimum number of attempts needed for {m} eggs and {n} floors is: {result}")