def boyer_moore(nums: List[int]) -> int:
    """
    使用摩尔投票法找出数组中的多数元素。
    
    参数:
        nums (List[int]): 输入的整数数组。
    
    返回:
        int: 数组中的多数元素。
    
    异常:
        ValueError: 如果没有元素的出现次数超过数组长度的一半。
    """
    # 初始阶段：候选人为空，计数器为0
    candidate = None
    count = 0

    # 第一阶段：找到可能的多数元素
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # 第二阶段：验证候选人是否为多数元素
    count = sum(1 for num in nums if num == candidate)
    
    # 确认候选人是否真的是多数元素
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No majority element found")