# ****************** 0/1 背包问题 ****************************
def zero_one_knapsack_naive(volumes, weights, capacity):
    """
    使用基本的动态规划解决0/1背包问题。
    参数:
        volumes: 物品体积列表
        weights: 物品价值列表
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j >= volumes[i - 1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-volumes[i-1]] + weights[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][capacity]
# ***********************************************************



# ****************** 0/1 背包问题 ****************************
def zero_one_knapsack_optimized1(volumes, weights, capacity):
    """
    使用滚动数组优化空间复杂度的动态规划解决0/1背包问题。
    参数:
        volumes: 物品体积列表
        weights: 物品价值列表
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    dp = [[0] * (capacity + 1) for _ in range(2)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            dp[i & 1][j] = dp[(i-1) & 1][j]
            if j >= volumes[i-1]:
                dp[i & 1][j] = max(dp[i & 1][j], dp[(i-1) & 1][j - volumes[i-1]] + weights[i-1])

    return dp[n & 1][capacity]
# ***********************************************************



# ****************** 0/1 背包问题 ****************************
def zero_one_knapsack_optimized2(volumes, weights, capacity):
    """
    使用一维数组进一步优化空间复杂度的动态规划解决0/1背包问题。
    参数:
        volumes: 物品体积列表
        weights: 物品价值列表
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # 从后往前遍历，确保每个物品只使用一次
        for j in range(capacity, volumes[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - volumes[i]] + weights[i])

    return max(dp)
# ***********************************************************



# ****************** 完全背包问题 ****************************
def complete_knapsack_naive(volumes, values, capacity):
    """
    使用二维数组解决完全背包问题的动态规划方法。
    完全背包问题允许每种物品可以无限次选择。
    
    参数:
        volumes: 物品体积列表
        values: 物品价值列表
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    # 初始化dp数组，所有值为0，dp[i][j]代表考虑前i个物品时，容量为j的背包的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 动态规划填表
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            dp[i][j] = dp[i-1][j]  # 不选择当前物品
            if j >= volumes[i - 1]:
                # 选择当前物品，因为是完全背包，所以可以继续选择i
                dp[i][j] = max(dp[i][j], dp[i][j - volumes[i - 1]] + values[i - 1])

    return dp[n][capacity]  # 返回dp数组中的最大值，即为背包的最大价值
# ************************************************************



# ****************** 完全背包问题 *****************************
def complete_knapsack_optimized(volumes, values, capacity):
    """
    使用一维数组进一步优化空间复杂度的动态规划解决完全背包问题。
    完全背包问题中，每种物品可以被无限次选取。
    
    参数:
        volumes: 物品体积列表
        values: 物品价值列表
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    # 初始化dp数组，所有值为0，dp[j]代表容量为j的背包的最大价值
    dp = [0] * (capacity + 1)

    # 动态规划填表
    for i in range(len(volumes)):
        for j in range(volumes[i], capacity + 1):
            # 从volumes[i]开始，因为容量小于volumes[i]不能装入该物品
            # 由于物品可以无限使用，遍历时从小到大更新dp[j]
            dp[j] = max(dp[j], dp[j - volumes[i]] + values[i])

    return dp[capacity]  # 返回dp数组中的最大值，即为背包的最大价值
# ***********************************************************



# ****************** 多重背包问题 ****************************
def multiple_knapsack_naive(volumes, values, counts, capacity):
    """
    使用二维数组解决多重背包问题的基础动态规划方法。
    参数:
        volumes: 物品体积列表
        values: 物品价值列表
        counts: 每种物品的数量
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(capacity + 1):
            dp[i][j] = dp[i-1][j]
            max_k = min(counts[i-1], j // volumes[i-1])
            for k in range(1, max_k + 1):
                dp[i][j] = max(dp[i][j], dp[i-1][j - k * volumes[i-1]] + k * values[i-1])

    return dp[n][capacity]
# ***********************************************************



# ****************** 多重背包问题 *****************************
def multiple_knapsack_optimized1(volumes, values, counts, capacity):
    """
    使用一维数组优化的动态规划解决多重背包问题。
    参数:
        volumes: 物品体积列表
        values: 物品价值列表
        counts: 每种物品的数量
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(1, counts[i] + 1):
            for k in range(capacity, volumes[i] - 1, -1):
                dp[k] = max(dp[k], dp[k - volumes[i]] + values[i])

    return max(dp)
# ***********************************************************



# ****************** 多重背包问题 ****************************
def multiple_knapsack_optimized2(volumes, values, counts, capacity):
    """
    使用二进制方法优化的多重背包问题解法。
    参数:
        volumes: 物品体积列表
        values: 物品价值列表
        counts: 每种物品的数量
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    items = []

    # 二进制拆分物品
    for i in range(n):
        k = 1
        while k <= counts[i]:
            items.append((volumes[i] * k, values[i] * k))
            counts[i] -= k
            k *= 2
        if counts[i] > 0:
            items.append((volumes[i] * counts[i], values[i] * counts[i]))

    dp = [0] * (capacity + 1)
    for volume, value in items:
        for j in range(capacity, volume - 1, -1):
            dp[j] = max(dp[j], dp[j - volume] + value)

    return dp[capacity]
# ************************************************************



# ****************** 多重背包问题 *****************************
def multiple_knapsack_optimized3(volumes, values, counts, capacity):
    """
    使用单调队列优化的多重背包问题解法。
    参数:
        volumes: 物品体积列表
        values: 物品价值列表
        counts: 每种物品的数量
        capacity: 背包的容量
    返回:
        背包能达到的最大价值
    """
    n = len(volumes)
    dp = [0] * (capacity + 1)  # 正确初始化列表

    for i in range(n):
        for mod in range(volumes[i]):
            queue = []
            max_range = (capacity - mod) // volumes[i]
            for k in range(max_range + 1):
                val = dp[k * volumes[i] + mod] - k * values[i]
                
                # 维护单调队列，保持队列中的元素单调递减
                while queue and queue[-1][1] <= val:
                    queue.pop()
                queue.append((k, val))
                
                # 若队首元素超出了滑动窗口范围，即移除过时元素
                if queue[0][0] < k - counts[i]:
                    queue.pop(0)
                
                # 计算当前容量下的最大价值
                dp[k * volumes[i] + mod] = queue[0][1] + k * values[i]

    return dp[capacity]
# *************************************************************



# ****************** 分组背包问题 ******************************
def group_knapsack(max_capacity, groups_items):
    """
    计算在给定的最大容量下，通过选择每组中的一个物品可以获得的最大价值。
    
    参数:
        max_capacity: 整数，表示背包的最大容量
        groups_items: 二维列表，每个子列表表示一组物品，子列表中的每个元素为元组 (volume, value)
        
    返回:
        整数，表示在最大容量下可以获得的最大价值
    """
    dp = [0] * (max_capacity + 1)
    for items in groups_items:
        for current_capacity in range(max_capacity, -1, -1):
            for volume, value in items:
                if volume <= current_capacity:
                    dp[current_capacity] = max(dp[current_capacity], dp[current_capacity - volume] + value)

    return dp[max_capacity]
# **************************************************************