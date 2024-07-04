def zero_one_knapsack_naive(volumes, weights, capacity):
    n = len(volumes)
    # 创建dp表
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填充dp表
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j >= volumes[i - 1]:  # 检查当前容量是否可以容纳物品i
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-volumes[i-1]] + weights[i-1])
            else:
                dp[i][j] = dp[i-1][j]  # 不添加当前物品

    return dp[n][capacity]



def zero_one_knapsack_optimized1(volumes, weights, capacity):
    n = len(volumes)
    # 使用两行滚动数组
    dp = [[0] * (capacity + 1) for _ in range(2)]

    # 动态规划填表
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            # 不放入当前物品
            dp[i & 1][j] = dp[(i-1) & 1][j]
            # 放入当前物品，前提是当前容量能容纳当前物品
            if j >= volumes[i-1]:
                dp[i & 1][j] = max(dp[i & 1][j], dp[(i-1) & 1][j - volumes[i-1]] + weights[i-1])

    # 最终结果存储在dp[n & 1][capacity]
    return dp[n & 1][capacity]



def zero_one_knapsack_optimized2(volumes, weights, capacity):
    n = len(volumes)
    # 初始化dp数组，所有值为0
    dp = [0] * (capacity + 1)

    # 动态规划填表
    for i in range(n):
        # 从后往前遍历，确保每个物品只使用一次
        for j in range(capacity, volumes[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - volumes[i]] + weights[i])


    return max(dp)


if __name__ == "__main__":
    n, capacity = map(int, input().split())

    volumes = []
    weights = []

    for i in range(n):
        v, w = map(int, input().split())
        volumes.append(v)
        weights.append(w)

    max_value = zero_one_knapsack_optimized2(volumes, weights, capacity)
    print(max_value)