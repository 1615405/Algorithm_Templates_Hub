def majorityElement(nums):
    """
    利用摩尔投票法找出列表中的多数元素。多数元素是指在数组中出现次数超过一半的元素。

    参数：
        nums (List[int]): 输入的整数列表。

    返回：
        int: 数组中的多数元素。
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
    
    if count > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No majority element found")
