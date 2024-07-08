# ****************** 最大子数组和问题 ******************
def maxSubArray(nums: List[int]) -> int:
    """
    使用 Kadane 算法找出给定整数数组中的最大子数组和。
    参数:
        nums: 整数数组
    返回:
        最大子数组的和
    """
    current_max = global_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)
    
    return global_max
# **************************************************



# ****************** 数字三角形问题 ******************
def digital_triangle_problem(triangle: List[List[int]]) -> int:
    """
    解决数字三角形问题，找出自顶向下的路径，使该路径上的数字之和最大。这个方法采用自底向上的动态规划策略，
    避免了自顶向下可能遇到的复杂边界问题，并减少了重复计算。

    参数:
        triangle: 一个二维列表，表示数字三角形，其中 triangle[i][j] 是三角形第 i 行第 j 列的数字。

    返回:
        int: 从三角形顶部到底部的最大路径和。
    """
    n = len(triangle)
    
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
            
    return triangle[0][0]
# **************************************************



# ****************** 网格路径最大和问题 ******************
def max_path_sum(grid) -> int:
    """
    解决在一个 n x m 的网格中，从左上角到右下角取得最大路径和的问题。每个单元格包含一个整数，可以向下或向右移动。

    参数:
        grid: 二维列表，表示每个单元格中的数值。

    返回:
        int: 从左上角到右下角可以取得的最大路径和。
    """
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]

    # 初始化第一个单元格
    dp[0][0] = grid[0][0]

    # 初始化第一行
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # 初始化第一列
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # 动态规划填表
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[n - 1][m - 1]
# **************************************************



# ****************** 同时移动两个人的网格收集最大数值问题 ******************
def max_dual_path_sum(n, m, grid):
    """
    解决在一个 n x m 的网格中，同时移动两个人从 (1,1) 到 (n,m)，使得他们通过的路径的总数值最大化的问题。
    每一步两个人可以向下或向右移动，但不能在同一时刻占据同一个格子，除了在起点和终点。

    参数:
        n: 网格的行数
        m: 网格的列数
        grid: 二维列表，表示每个单元格中的数值

    返回:
        int: 从 (1,1) 到 (n,m) 两个人可以收集到的最大数值。
    """
    # 创建一个 (n+m+1) x (n+1) x (n+1) 的三维数组 f，用于动态规划存储到达每个单元格的最大数值
    f = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + m + 1)]

    # 动态规划填表
    for k in range(2, n + m + 1):
        for i1 in range(1, min(n, k - 1) + 1):
            for i2 in range(1, min(n, k - 1) + 1):
                j1 = k - i1
                j2 = k - i2
                if 1 <= j1 <= m and 1 <= j2 <= m:
                    # 避免两人占据同一格子，除非是起点或终点
                    if i1 == i2 and k != m + n:
                        continue
                    # 计算当前步骤的数值
                    val = grid[i1 - 1][j1 - 1] + (grid[i2 - 1][j2 - 1] if i1 != i2 else 0)

                    # 更新动态规划表
                    f[k][i1][i2] = max(
                        f[k][i1][i2],
                        f[k - 1][i1 - 1][i2 - 1] + val,
                        f[k - 1][i1 - 1][i2] + val,
                        f[k - 1][i1][i2 - 1] + val,
                        f[k - 1][i1][i2] + val
                    )

    # 返回最后一个单元格的数值，即两人同时到达终点的最大数值
    return f[n + m][n][n]
# ***************************************************************



# ****************** 最长递增子序列问题 ******************
def longest_increasing_subsequence(arr: List[int]) -> int:
    """
    计算给定数组中最长递增子序列的长度。这个动态规划算法考虑了数组中每个元素作为潜在的递增子序列的结束点，
    并试图找到包含该元素的最长子序列。

    参数:
        arr: 整数数组，其中需要找出最长递增子序列。

    返回:
        int: 数组中最长递增子序列的长度。
    """
    n = len(arr)
    lis_lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)
                
    return max(lis_lengths)
# **************************************************



# ****************** 最长递增子序列问题 (贪心 + 二分查找) ******************
def longest_increasing_subsequence(nums):
    """
    使用贪心算法和二分查找来找出给定整数数组中的最长递增子序列的长度。
    此方法不记录具体的子序列，而是维护一个列表，其中每个位置 i 保存长度为 i+1 的所有
    上升子序列中最小的末尾元素。

    参数:
        nums: 整数数组，其中需要找出最长递增子序列。

    返回:
        int: 数组中最长递增子序列的长度。
    """
    from bisect import bisect_left

    tails = []  # 用于保存每个长度上升子序列可能的最小末尾元素
    for num in nums:
        # 使用二分查找确定当前数字 num 应插入的位置
        idx = bisect_left(tails, num)  # 找到 num 应该插入的位置
        if idx == len(tails):          # 如果 num 大于所有已记录的末尾，形成新的更长子序列
            tails.append(num)
        else:
            tails[idx] = num           # 更新现有序列的可能最小末尾元素
        
    return len(tails)  # 最长上升子序列的长度为 tails 列表的长度
# ***************************************************************



# ****************** 最长公共子序列问题 ******************
def longest_common_subsequence(a, b):
    """
    计算两个字符串 a 和 b 的最长公共子序列的长度。使用动态规划方法，
    构建一个二维数组 dp，其中 dp[i][j] 表示字符串 a 的前 i 个字符和
    字符串 b 的前 j 个字符的最长公共子序列的长度。

    参数:
        a: 第一个字符串
        b: 第二个字符串

    返回:
        int: 两个字符串的最长公共子序列的长度。
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # 初始化动态规划表格

    # 填充 dp 表格
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 如果字符不匹配，取上方或左方的最大值
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            # 如果字符匹配，考虑对角线上的值加一
            if a[i - 1] == b[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

    return dp[n][m]  # dp表的最后一个元素存储了问题的解
# **************************************************



# ****************** 编辑距离问题 ******************
def edit_distance(s1: str, s2: str) -> int:
    """
    计算两个字符串 s1 和 s2 之间的编辑距离。编辑距离是将一个字符串转换成另一个字符串所需的最少编辑操作次数，
    其中允许的操作包括插入一个字符、删除一个字符或替换一个字符。

    参数:
        s1: 第一个字符串
        s2: 第二个字符串

    返回:
        int: 两个字符串之间的编辑距离。
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化dp数组的第一行和第一列
    for i in range(m + 1):
        dp[i][0] = i  # 将 s1 转换为空字符串 s2 需要 i 次删除操作
    for j in range(n + 1):
        dp[0][j] = j  # 将空字符串 s1 转换为 s2 需要 j 次插入操作

    # 动态规划处理所有的子问题
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 当前字符相同，不需要编辑操作
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # 删除操作
                    dp[i][j - 1],    # 插入操作
                    dp[i - 1][j - 1] # 替换操作
                )

    return dp[m][n]  # 返回整个 dp 表的最后一个元素，即编辑距离的最小值
# **************************************************



# ****************** 最长公共上升子序列问题 ******************
def longest_increasing_common_subsequence(a, b):
    """
    计算两个字符串之间的最长公共上升子序列的长度。
    
    参数:
        a: 第一个字符串
        b: 第二个字符串

    返回:
        int: 两个字符串的最长公共上升子序列的长度。
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        maxv = 1
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] == b[j - 1]:
                dp[i][j] = max(dp[i][j], maxv)
            if b[j - 1] < a[i - 1]:
                maxv = max(maxv, dp[i - 1][j] + 1)

    result = max(dp[m][i] for i in range(1, n + 1))
    return result
# ***************************************************************



# ****************** 最少非严格递减子序列问题 ******************
def min_non_increasing_subsequences(numbers):
    """
    计算给定数字序列所需的最少数量的非严格递减子序列。这是一个动态规划问题，可以通过维护
    一个列表来解决，该列表中的每个元素表示当前找到的非严格递减子序列的最小末尾元素。

    参数:
        numbers: 整数列表，表示需要处理的数字序列。

    返回:
        int: 最少可以将序列分割成的非严格递减子序列的数量。
    """
    from bisect import bisect_left
    
    tails = []  # 用于存储每个非严格递减子序列的末尾元素
    for number in numbers:
        # 找到可以放置当前数字的位置，保持非严格递减
        pos = bisect_left(tails, number)
        if pos < len(tails):
            tails[pos] = number  # 更新这个位置的末尾元素为当前数字
        else:
            tails.append(number)  # 如果没有合适的位置，新增一个子序列

    return len(tails)  # 返回子序列的数量
# ***************************************************************



# ****************** 最小双条件序列分割问题 ******************
def minimal_partition_dfs(idx, inc, dec):
    """
    使用深度优先搜索来计算将元素序列分割成两种不同排序条件的子序列的最小数量。
    这个函数通过递归地尝试每种可能的分割方法，寻找将序列分割成满足这两种条件的子序列的最少数量。

    参数:
    idx (int): 当前处理的元素索引，指示正在处理序列中的哪一个元素。
    inc (int): 当前按第一种条件（如递增）分割的子序列数量。
    dec (int): 当前按第二种条件（如递减）分割的子序列数量。

    函数依赖全局变量：
    - result (int): 存储到目前为止找到的最小分割数量。
    - elements (list): 待分割的元素序列。
    - last_inc (list): 存储每个满足第一条件的子序列的最后一个元素。
    - last_dec (list): 存储每个满足第二条件的子序列的最后一个元素。
    """
    global result, elements, last_inc, last_dec

    # 剪枝：如果当前分割的子序列数已超过已知的最小值，停止递归
    if inc + dec >= result:
        return

    # 如果所有元素都已处理完，更新全局最小值
    if idx == len(elements):
        result = min(result, inc + dec)
        return

    # 尝试将当前元素加入第一种条件的子序列
    k = 0
    while k < inc and elements[idx] <= last_inc[k]:
        k += 1
    temp = last_inc[k]
    last_inc[k] = elements[idx]
    if k < inc:
        minimal_partition_dfs(idx + 1, inc, dec)
    else:
        minimal_partition_dfs(idx + 1, inc + 1, dec)
    last_inc[k] = temp

    # 尝试将当前元素加入第二种条件的子序列
    k = 0
    while k < dec and elements[idx] >= last_dec[k]:
        k += 1
    temp = last_dec[k]
    last_dec[k] = elements[idx]
    if k < dec:
        minimal_partition_dfs(idx + 1, inc, dec)
    else:
        minimal_partition_dfs(idx + 1, inc, dec + 1)
    last_dec[k] = temp
# *************************************************