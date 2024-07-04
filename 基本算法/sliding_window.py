def length_of_longest_substring(s: str) -> int:
    """
    计算给定字符串中最长无重复字符的子串的长度。
    """
    max_length = 0  # 存储最长子串的长度
    left = 0  # 滑动窗口的左边界
    char_set = set()  # 存储当前无重复字符的集合

    for right, char in enumerate(s):
        # 如果字符已在集合中，逐个移除窗口左侧的字符，直到该字符可以被添加进集合
        while left <= right and char in char_set:
            char_set.remove(s[left])
            left += 1
        # 将当前字符添加到集合中
        char_set.add(char)
        # 更新最大长度
        max_length = max(max_length, right - left + 1)

    return max_length



def maxArea(height: List[int]) -> int:
    """
    计算由线段垂直于x轴和两个点形成的容器可以容纳的最大水量。
    使用双指针法，从数组的两端开始向中心移动，每次移动较短的一端，以尝试找到更大的容积。
    """
    max_area = 0  # 初始化最大面积为0
    left, right = 0, len(height) - 1  # 初始化双指针位置
    
    while left < right:
        # 计算当前双指针对应的容器面积
        current_area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, current_area)  # 更新最大面积
        
        # 移动较短的一端的指针
        if height[left] <= height[right]:
            left += 1  # 左指针向右移动
        else:
            right -= 1  # 右指针向左移动

    return max_area