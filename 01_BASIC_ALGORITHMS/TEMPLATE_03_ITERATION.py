def findShortestSubArray(nums: List[int]) -> int:
    """
    计算具有与整个数组相同的度的最短子数组的长度。
    """
    first, last = {}, {}  # 存储每个元素的第一次和最后一次出现的索引
    count = Counter(nums)  # 计算每个元素的出现频率

    # 遍历数组，记录每个元素的第一次和最后一次出现的位置
    for i, num in enumerate(nums):
        if num not in first:
            first[num] = i  # 记录第一次出现的索引
        last[num] = i  # 更新最后一次出现的索引
    
    degree = max(count.values())  # 数组的度，即任一元素的最大出现频率
    min_length = len(nums)  # 初始设置最小长度为数组的长度

    # 寻找具有相同度的最短子数组
    for num, cnt in count.items():
        if cnt == degree:
            min_length = min(min_length, last[num] - first[num] + 1)

    return min_length



def shortest_distance_to_char(s: str, target_char: str) -> List[int]:
    """
    计算字符串中每个字符到指定字符的最短距离。
    """
    n = len(s)
    min_distances = [float('inf')] * n  # 初始化距离数组为无限大
    
    # 从左向右遍历，记录到最近左侧 target_char 的距离
    last_seen_left = float('-inf')  # 初始化为-inf，表示尚未遇到 target_char
    for i in range(n):
        if s[i] == target_char:
            last_seen_left = i
        min_distances[i] = i - last_seen_left
    
    # 从右向左遍历，记录到最近右侧 target_char 的距离，并取最小值
    last_seen_right = float('inf')  # 初始化为inf，表示尚未遇到 target_char
    for i in range(n-1, -1, -1):
        if s[i] == target_char:
            last_seen_right = i
        min_distances[i] = min(min_distances[i], last_seen_right - i)
    
    return min_distances