def multiple_knapsack_naive(volumes, weights, counts, capacity):
    n = len(volumes)
    # 初始化dp数组，大小为 (n+1) x (capacity+1)，所有值初始化为0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 遍历每种物品
    for i in range(1, n + 1):
        # 遍历背包的每个容量
        for j in range(capacity + 1):
            # 初始化当前状态不包括当前物品的最大值
            dp[i][j] = dp[i-1][j]
            # 遍历当前物品可以放入的数量，从1开始到最小的物品数量或最大能放入的次数
            max_k = min(counts[i-1], j // volumes[i-1])
            for k in range(1, max_k + 1):
                # 更新dp[i][j]的值，考虑放入k个当前物品
                dp[i][j] = max(dp[i][j], dp[i-1][j - k * volumes[i-1]] + k * weights[i-1])

    # 返回背包容量为capacity时的最大价值
    return dp[n][capacity]



def multiple_knapsack_optimized1(volumes, weights, counts, capacity):
    n = len(volumes)
    # 初始化dp数组，所有值为0（假设-无穷用0表示，因为不可能取负值）
    dp = [0] * (capacity + 1)

    # 遍历每个物品
    for i in range(n):
        # 对当前物品可用的每个数量
        for j in range(1, counts[i] + 1):
            # 从大到小更新背包容量，确保不重复计算物品
            for k in range(capacity, volumes[i] - 1, -1):
                dp[k] = max(dp[k], dp[k - volumes[i]] + weights[i])

    # 寻找最大值
    return max(dp)



def multiple_knapsack_optimized2(volumes, weights, counts, capacity):
    # volumes, weights, counts 分别为物品体积、权重和数量列表，capacity为背包容量
    n = len(volumes)
    items = []

    # 二进制拆分物品
    for i in range(n):
        k = 1
        while k <= counts[i]:
            items.append((volumes[i] * k, weights[i] * k))
            counts[i] -= k
            k *= 2
        if counts[i] > 0:
            items.append((volumes[i] * counts[i], weights[i] * counts[i]))

    # 初始化dp数组
    dp = [0] * (capacity + 1)

    # 0-1背包处理
    for volume, weight in items:
        for j in range(capacity, volume - 1, -1):
            dp[j] = max(dp[j], dp[j - volume] + weight)

    return dp[capacity]
    
    

def multiple_knapsack_optimized3(volumes, weights, counts, capacity):
    n = len(volumes)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for mod in range(volumes[i]):
            # 使用单调队列优化
            queue = []
            max_range = (capacity - mod) // volumes[i]
            for k in range(max_range + 1):
                val = dp[k * volumes[i] + mod] - k * weights[i]
                
                # 维护队列为单调递减
                while queue and queue[-1][1] <= val:
                    queue.pop()
                queue.append((k, val))
                
                # 移除队首元素（如果不在有效范围内）
                if queue[0][0] < k - counts[i]:
                    queue.pop(0)
                
                # 更新dp值
                dp[k * volumes[i] + mod] = queue[0][1] + k * weights[i]

    return dp[capacity]


if __name__ == "__main__":
    n, capacity = map(int, input().split())

    volumes = []
    weights = []
    counts = []
    
    for i in range(n):
        v, w, c = map(int, input().split())
        counts.append(c)
        volumes.append(v)
        weights.append(w)
        
    max_value = multiple_knapsack_naive(volumes, weights, counts, capacity)
    print(max_value)