def maxArea(height: List[int]) -> int:
    """
    计算由线段垂直于x轴和两个点形成的容器可以容纳的最大水量。
    
    使用双指针法，从数组的两端开始向中心移动，每次移动较短的一端，以尝试找到更大的容积。
    
    参数:
        height (List[int]): 每个位置的高度。
    
    返回:
        int: 最大的水容量。
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
