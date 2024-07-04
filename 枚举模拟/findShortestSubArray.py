def shortest_distance_to_char(self, s: str, target_char: str) -> List[int]:
    """
    计算字符串中每个字符到指定字符的最短距离。
    
    参数:
        s (str): 输入的字符串。
        target_char (str): 指定的字符，计算到此字符的距离。
    
    返回:
        List[int]: 每个字符到指定字符的最短距离列表。
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