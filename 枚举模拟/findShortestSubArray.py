def findShortestSubArray(self, nums: List[int]) -> int:
        """
        计算具有与整个数组相同的度的最短子数组的长度。
        
        参数:
            nums (List[int]): 输入的整数数组。
            
        返回:
            int: 具有相同度的最短子数组的长度。
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