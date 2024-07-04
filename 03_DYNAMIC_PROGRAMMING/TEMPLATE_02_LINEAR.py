def greedy_longest_increasing_seq(nums):
    """
    贪心算法：
    在这种优化方法中，贪心算法的应用体现在对每个可能的上升子序列长度维持一个可能的最小的末尾元素
    的决策上。每次我们尝试使用尽可能小的元素来更新或扩展这些序列。这种做法确保了任何时候，对于
    相同长度的上升子序列，我们总是记录下具有最小末尾元素的那个序列。这不仅让当前序列的末尾尽可能小，
    而且为未来可能的更长上升子序列的构建留下了空间。

    二分查找：
    通过使用二分查找，我们能够快速确定一个新元素应该插入的位置，即它可以代替哪个序列的末尾元素
    或者它可以形成新的序列长度。

    并未直接记录每个具体的子序列，而是通过 tails 记录了达到每个可能长度的子序列的最优末尾元素。
    """
    tails = []
    for num in nums:
        idx = bisect_left(tails, num)  # 使用二分查找确定插入位置
        if idx == len(tails):          # 如果是新的更长序列，添加到末尾
            tails.append(num)
        else:
            tails[idx] = num           # 否则更新存在的位置
    return len(tails)                  # 返回最长上升子序列的长度



def longest_increasing_subsequence(arr: List[int]) -> int:
    """
    计算给定数组中最长递增子序列的长度。
    """
    n = len(arr)
    if n == 0:
        return 0

    lis_lengths = [1] * n  # 存储每个元素的最长子序列长度

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                lis_lengths[i] = max(lis_lengths[i], lis_lengths[j] + 1)

    return max(lis_lengths)



def longest_common_subsequence(a, b):
    """
    计算两个字符串a和b的最长公共子序列的长度。
    """
    n, m = len(a), len(b)
    f = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f[i][j] = max(f[i - 1][j], f[i][j - 1])
            if a[i - 1] == b[j - 1]:
                f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)

    return f[n][m]



def edit_distance(s1: str, s2: str) -> int:
    """
    计算两个字符串s1和s2之间的编辑距离。
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化dp数组
    for i in range(m + 1):
        dp[i][0] = i  # s1转换为空字符串
    for j in range(n + 1):
        dp[0][j] = j  # 空字符串转换为s2

    # 动态规划填表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 字符相同，不增加操作
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # 删除
                    dp[i][j - 1],    # 插入
                    dp[i - 1][j - 1] # 替换
                )

    return dp[m][n]



def digital_triangle_problem(triangle: List[List[int]]) -> int:
    """
    解决数字三角形问题，找出自顶向下的路径，使该路径上的数字之和最大。
    """
    n = len(triangle)
    
    # 自底向上计算每个位置的最大路径和，从倒数第二行开始枚举
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    return triangle[0][0]