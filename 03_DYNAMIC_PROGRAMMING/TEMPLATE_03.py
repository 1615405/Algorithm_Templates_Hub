# ****************** 合并石子问题（区间动态规划） ******************
def merge_stones_problem(num_stones, stones):
    """
    计算将石子合并成一堆的最小成本，使用区间动态规划算法。
    
    参数:
        num_stones: 整数，表示石子的数量
        stones: 整数列表，表示每堆石子的数量
        
    返回:
        整数，表示将所有石子合并成一堆的最小成本
    """
    # 初始化前缀和数组和动态规划数组
    prefix_sum = [0] * (num_stones + 1)
    dp = [[float('inf')] * (num_stones + 1) for _ in range(num_stones + 1)]

    # 计算前缀和，便于后续快速计算区间和
    for i in range(1, num_stones + 1):
        prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]

    # 初始化单个石子合并成本为0
    for i in range(1, num_stones + 1):
        dp[i][i] = 0

    # 使用动态规划寻找最小合并成本
    for length in range(2, num_stones + 1):  # 枚举区间长度
        for l in range(1, num_stones - length + 2):  # 枚举区间起点
            r = l + length - 1
            # 枚举分割点，计算最小成本
            for k in range(l, r):  
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + prefix_sum[r] - prefix_sum[l - 1])

    return dp[1][num_stones]
# ********************************************************************



# ****************** 计数分割方案（完全背包问题） **********************
def count_partitions(n, mod=10**9+7):
    """
    计算将整数 n 分割成若干个部分的方案数，使用完全背包问题的动态规划算法。
    
    参数:
        n: 整数，表示需要分割的数
        mod: 整数，表示取模数，默认值为 10**9 + 7
        
    返回:
        整数，表示将 n 分割成若干个部分的方案数
    """
    f = [0] * (n + 1)
    # 基础情况：将数字0分割的方式有1种（不取任何数）
    f[0] = 1
    
    # 完全背包问题
    for i in range(1, n + 1):  # 枚举物品序号
        for j in range(i, n + 1):  # 正序枚举背包体积
            f[j] = (f[j] + f[j - i]) % mod
    
    return f[n]
# *******************************************************************



# ****************** 数位动态规划计算数字出现次数 ******************
def countDigitX(n: int, x: int) -> int:
    """
    计算 1 到 n 中任意数字 x 出现的次数。
    
    参数:
        n: 整数，表示范围上限
        x: 整数，表示需要统计的数字
        
    返回:
        整数，表示 x 在 1 到 n 中出现的次数
    """
    digit, result = 1, 0  # 初始化当前位因子和结果
    high, cur, low = n // 10, n % 10, 0  # 分别初始化高位、当前位和低位

    # 循环处理每一位，直到所有高位和当前位都被处理完
    while high or cur:
        if cur < x:
            # 当前位小于 x，x 出现次数只由高位决定
            result += high * digit
        elif cur == x:
            # 当前位等于 x，x 出现次数由高位和低位共同决定
            result += high * digit + low + 1
            # 特殊情况：当 x 为 0 时，需要减去多算的前导 0
            if x == 0:
                result -= digit if high > 0 else 0
        else:
            # 当前位大于 x，x 出现次数由高位决定，需要加上当前位
            result += (high + (x > 0)) * digit

        # 更新低位、当前位、高位和位因子，以处理下一个更高位
        low += cur * digit  # 将当前位的值加到低位上
        cur = high % 10  # 更新当前位为高位的最低位
        high //= 10  # 去掉高位的最低位
        digit *= 10  # 位因子乘以 10，以处理下一个更高位

    return result
# ******************************************************************



# ****************** 状态压缩动态规划 - 覆盖棋盘问题 ******************
def count_tilings(n, m):
    """
    计算完全覆盖 n x m 棋盘的方法数，使用 1x2 的多诺米骨牌。
    
    参数:
        n: 整数，表示棋盘的行数
        m: 整数，表示棋盘的列数
        
    返回:
        整数，表示覆盖整个棋盘的方法数
    """
    def is_valid_state(state, n):
        cnt = 0
        for j in range(n):
            if state & (1 << j):  # 检查第 j 位是否被设置（覆盖）
                if cnt & 1:  # 如果连续未覆盖的数目为奇数
                    return False
                cnt = 0
            else:
                cnt += 1
        return cnt & 1 == 0  # 检查最后的未覆盖部分是否为偶数
    
    M = 1 << n  # 所有可能的状态数
    valid = [False] * M  # 每个状态的有效性
    state_transitions = [[] for _ in range(M)]  # 状态转移列表
    dp = [[0] * M for _ in range(m + 1)]  # 动态规划表

    # 确定哪些状态是有效的
    for i in range(M):
        valid[i] = is_valid_state(i, n)

    # 构建可能的状态转移
    for i in range(M):
        for j in range(M):
            if (i & j) == 0 and valid[i | j]:  # 确保没有重叠且组合状态有效
                state_transitions[i].append(j)

    # 初始化动态规划表
    dp[0][0] = 1  # 开始时有一种方法（不放置瓷砖）

    # 填充动态规划表
    for i in range(1, m + 1):
        for j in range(M):
            for k in state_transitions[j]:  # 遍历所有可以转移到 j 的状态
                dp[i][j] += dp[i - 1][k]  # 增加达到状态 j 的方法数

    return dp[m][0]  # 返回覆盖整个棋盘的方法数
# *******************************************************************



# ****************** 最小汉密尔顿回路问题（TSP - 状态压缩动态规划） ******************
def minimize_hamiltonian_circuit(n, weights):
    """
    解决旅行商问题（TSP），使用状态压缩的动态规划方法。
    
    参数:
        n: 整数，表示城市数量
        weights: 二维列表，表示城市间的路径权重
        
    返回:
        整数，表示访问所有城市并返回起点的最小成本
    """
    state_num = 1 << n  # 总状态数，每个状态代表一个城市的访问状态
    f = [[float('inf')] * n for _ in range(state_num + 1)]  # 动态规划数组

    f[1][0] = 0  # 初始化起点城市，即从城市0开始，只访问城市0的最小成本为0

    # 动态规划状态转移
    for i in range(state_num):
        for j in range(n):
            if (i >> j) & 1:  # 当前状态i中，城市j是否被访问过
                for k in range(n):
                    if (i >> k) & 1 and k != j:  # 确保城市k在当前状态被访问过且不是城市j
                        f[i][j] = min(f[i][j], f[i - (1 << j)][k] + weights[k][j])  # 状态转移，更新成本

    return f[(1 << n) - 1][n - 1]  # 返回访问所有城市并返回起点的最小成本
# **************************************************



# ****************** 树形DP - 最大快乐值问题 ******************
def dfs(u):
    dp[u][1] = happy[u]  # 如果选择当前节点
    for v in children[u]:
        dfs(v)
        dp[u][1] += dp[v][0]  # 当前节点选择时，累加子节点不选择时的快乐值
        dp[u][0] += max(dp[v][0], dp[v][1])  # 当前节点不选择时，累加子节点选择或不选择中的最大快乐值
# ************************************************************



def longest_skiing_path(n, m, matrix):
    """
    计算在一个 n x m 的矩阵中，从每个点出发的最长递减路径长度。
    
    参数:
        n: 整数，表示矩阵的行数
        m: 整数，表示矩阵的列数
        matrix: 二维列表，表示高度矩阵
        
    返回:
        整数，表示最长递减路径的长度
    """
    from functools import lru_cache
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    @lru_cache(None)
    def dp(x, y):
        max_length = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[x][y] > matrix[nx][ny]:
                max_length = max(max_length, dp(nx, ny) + 1)
        return max_length

    result = 0
    for i in range(n):
        for j in range(m):
            result = max(result, dp(i, j))

    return result
# **************************************************