def complete_knapsack_naive(volumes, values, capacity):
    n = len(volumes)
    # 创建dp表
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 动态规划填表
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            # 初始化当前状态不包含当前物品的最大值
            dp[i][j] = dp[i-1][j]
            # 如果当前容量可以包含至少一个当前物品
            if j >= volumes[i - 1]:
                # 选择不放入当前物品和放入若干个当前物品的最大值
                dp[i][j] = max(dp[i][j], dp[i][j - volumes[i - 1]] + values[i - 1])

    return dp[n][capacity]



def complete_knapsack_optimized(volumes, values, capacity):
    # 创建一维dp数组，初始化为0
    dp = [0] * (capacity + 1)

    # 动态规划填表
    # 遍历所有物品
    for i in range(len(volumes)):
        # 正序循环，从当前物品的体积开始直到背包的最大容量
        for j in range(volumes[i], capacity + 1):
            # 更新dp[j]为选取或不选取当前物品的最大值
            # dp[j - volumes[i]] + values[i]表示加入一个当前物品i后的价值
            dp[j] = max(dp[j], dp[j - volumes[i]] + values[i])

    return dp[capacity]


if __name__ == "__main__":
    n, capacity = map(int, input().split())

    volumes = []
    weights = []

    for i in range(n):
        v, w = map(int, input().split())
        volumes.append(v)
        weights.append(w)
        
    max_value = complete_knapsack_optimized(volumes, weights, capacity)
    print(max_value)