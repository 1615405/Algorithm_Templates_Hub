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