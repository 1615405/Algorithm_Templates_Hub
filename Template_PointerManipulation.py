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


def isHappy(n: int) -> bool:
    """
    判断一个整数 n 是否是快乐数。快乐数的定义：在重复替换数字以其数字的平方和的过程中，如果 n 最终等于 1，则 n 是快乐数。

    参数:
        n (int): 需要判断的整数。

    返回:
        bool: 如果 n 是快乐数，则返回 True，否则返回 False。
    """
    def get_next(x: int) -> int:
        total_sum = 0
        while x:
            x, v = divmod(x, 10)
            total_sum += v * v
        return total_sum
    
    slow = n
    fast = get_next(n)
    while slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return slow == 1


def summaryRanges(nums: List[int]) -> List[str]:
    """
    汇总数组中连续的整数范围，并以字符串形式返回。例如，数组 [0,1,2,4,5,7] 将被汇总为 ["0->2","4->5","7"]。

    参数:
        nums (List[int]): 一个整数数组。

    返回:
        List[str]: 表示连续整数范围的字符串列表。
    """
    ans = []
    n, i = len(nums), 0
    while i < n:
        start = i
        while i < n - 1 and nums[i] + 1 == nums[i + 1]:
            i += 1
        s = str(nums[start])
        if start < i:
            s += "->" + str(nums[i])
        ans.append(s)
        i += 1
    return ans


def reverseVowels(s: str) -> str:
    """
    反转字符串中的所有元音字母。
    
    参数:
        s (str): 输入的字符串。
        
    返回:
        str: 元音字母被反转后的字符串。
    """
    def isVowel(ch: str) -> bool:
        return ch in "aeiouAEIOU"
    
    left, right = 0, len(s) - 1
    slist = list(s)
    while left < right:
        while left < right and not isVowel(s[left]):
            left += 1
        while left < right and not isVowel(s[right]):
            right -= 1
        if left < right:
            slist[left], slist[right] = slist[right], slist[left]
        left += 1
        right -= 1
    return ''.join(slist)


def findMaxAverage(nums: List[int], k: int) -> float:
    """
    计算数组中长度为 k 的连续子数组的最大平均值。

    参数:
        nums (List[int]): 一个整数数组。
        k (int): 子数组的固定长度。

    返回:
        float: 最大平均值。

    方法:
        使用滑动窗口算法，维护一个长度为 k 的窗口，计算并更新该窗口的总和，
        以此找到最大的窗口总和，并返回其平均值。
    """
    maxTotal = total = sum(nums[:k])
    for i in range(k, len(nums)):
        total = total - nums[i - k] + nums[i]
        maxTotal = max(maxTotal, total)
    return maxTotal / k


def shortestToChar(s: str, c: str) -> List[int]:
    """
    计算并返回字符串 s 中每个字符到最近的字符 c 的最短距离。
    """
    n = len(s)
    ans = [float('inf')] * n
    
    prev = float('-inf')
    for i in range(n):
        if s[i] == c:
            prev = i
        ans[i] = min(ans[i], i - prev)
    
    prev = float('inf')
    for i in range(n-1, -1, -1):
        if s[i] == c:
            prev = i
        ans[i] = min(ans[i], prev - i)
    
    return ans
