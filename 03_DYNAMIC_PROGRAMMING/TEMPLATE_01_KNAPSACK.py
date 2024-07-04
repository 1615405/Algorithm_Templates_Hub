def zero_one_knapsack_naive(volumes, weights, capacity):
    n = len(volumes)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j >= volumes[i - 1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-volumes[i-1]] + weights[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][capacity]



def zero_one_knapsack_optimized1(volumes, weights, capacity):
    n = len(volumes)
    dp = [[0] * (capacity + 1) for _ in range(2)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            dp[i & 1][j] = dp[(i-1) & 1][j]
            if j >= volumes[i-1]:
                dp[i & 1][j] = max(dp[i & 1][j], dp[(i-1) & 1][j - volumes[i-1]] + weights[i-1])

    return dp[n & 1][capacity]



def zero_one_knapsack_optimized2(volumes, weights, capacity):
    n = len(volumes)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(capacity, volumes[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - volumes[i]] + weights[i])

    return max(dp)





def complete_knapsack_naive(volumes, values, capacity):
    n = len(volumes)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            dp[i][j] = dp[i-1][j]
            if j >= volumes[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i][j - volumes[i - 1]] + values[i - 1])

    return dp[n][capacity]



def complete_knapsack_optimized(volumes, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(volumes)):
        for j in range(volumes[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - volumes[i]] + values[i])

    return dp[capacity]





def multiple_knapsack_naive(volumes, weights, counts, capacity):
    n = len(volumes)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            dp[i][j] = dp[i-1][j]
            max_k = min(counts[i-1], j // volumes[i-1])
            for k in range(1, max_k + 1):
                dp[i][j] = max(dp[i][j], dp[i-1][j - k * volumes[i-1]] + k * weights[i-1])

    return dp[n][capacity]



def multiple_knapsack_optimized1(volumes, weights, counts, capacity):
    n = len(volumes)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(1, counts[i] + 1):
            for k in range(capacity, volumes[i] - 1, -1):
                dp[k] = max(dp[k], dp[k - volumes[i]] + weights[i])

    return max(dp)



def multiple_knapsack_optimized2(volumes, weights, counts, capacity):
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





def group_knapsack(max_capacity, groups_items):
    dp = [0] * (max_capacity + 1)

    # 遍历所有物品组
    for items in groups_items:
        # 逆向遍历背包容量，确保每个物品只被计算一次
        for current_capacity in range(max_capacity, -1, -1):
            # 遍历当前组中的每个物品
            for volume, value in items:
                if volume <= current_capacity:
                    dp[current_capacity] = max(dp[current_capacity], dp[current_capacity - volume] + value)

    # 返回最大容量下的最大价值
    return dp[max_capacity]