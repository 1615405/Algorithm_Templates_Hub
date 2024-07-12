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


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    将两个有序数组合并为一个有序数组。第一个数组 nums1 的大小足以容纳合并后的数组，合并后的结果仍存放在 nums1 中。

    参数：
        nums1 (List[int]): 第一个有序数组，其长度至少为 m + n，其中前 m 个元素有效。
        m (int): nums1 中有效元素的数量。
        nums2 (List[int]): 第二个有序数组，长度为 n。
        n (int): nums2 中有效元素的数量。
    
    说明：
        不返回任何内容，而是直接在 nums1 中就地修改。
    """
    p1, p2 = m - 1, n - 1  # 初始化两个数组的指针，指向最后一个有效元素
    tail = m + n - 1       # 初始化合并后数组的最后一个位置的指针

    while p1 >= 0 or p2 >= 0:  # 只要有一个数组还有元素未处理就继续
        if p1 == -1:
            nums1[tail] = nums2[p2]
            p2 -= 1
        elif p2 == -1:
            nums1[tail] = nums1[p1]
            p1 -= 1
        elif nums1[p1] > nums2[p2]:
            nums1[tail] = nums1[p1]
            p1 -= 1
        else:
            nums1[tail] = nums2[p2]
            p2 -= 1
        tail -= 1  # 更新尾部指针
