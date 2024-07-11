def removeDuplicates(nums: List[int]) -> int:
    """
    从排序数组中删除重复项，并返回新的数组长度。
    此函数在原数组上直接修改，并使用双指针技术，一个快指针和一个慢指针来实现。

    参数：
        nums (List[int]): 输入的已排序整数数组。
    
    返回：
        int: 数组修改后的新长度，数组前该长度内的元素为去重后的结果。
    """
    n = len(nums)
    fast = 1  # 快指针，用于遍历数组
    slow = 1  # 慢指针，用于记录去重后的位置

    while fast < n:
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]  # 发现不同元素时，复制到慢指针的位置
            slow += 1  # 慢指针移动
        fast += 1  # 快指针始终移动
    
    return slow  # 返回新的数组长度
