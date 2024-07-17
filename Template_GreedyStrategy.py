def max_disjoint_intervals(intervals: List[List[int]]) -> int:
    """
    解决区间选点问题以及最大不相交区间数量问题。

    功能说明：
        - 区间选点问题：从给定的闭区间集合中选择尽可能少的点，使得每个区间至少包含一个点。函数返回所需的最小点数。
        - 最大不相交区间问题：从给定的闭区间集合中选择最多的互不相交区间。函数返回最大的可选区间数量。

    算法思路：
        1. 首先对区间按照每个区间的结束点进行升序排序。这是因为，早结束的区间较少限制后续区间的选择。
        2. 初始化一个记录最后被覆盖区间结束点的变量（last_covered_end），设置为负无穷，表示开始时没有任何区间被覆盖。
        3. 遍历排序后的区间列表，对于每个区间，检查其开始点是否大于 last_covered_end：
           - 如果是，说明当前区间与之前选中的区间不相交，需要选择一个新的点（通常选择当前区间的结束点，因为这可以最大化后续区间的覆盖可能）。
           - 更新 last_covered_end 为当前区间的结束点，并将这个点加入到选点列表中。
        4. 最终，返回列表中点的数量，该数量即为解决上述两个问题的答案。
    """
    intervals.sort(key=lambda x: x[1])
    points = []
  
    last_covered_end = float('-inf')
    for start, end in intervals:
        if start > last_covered_end:
            last_covered_end = end
            points.append(last_covered_end)
  
    return len(points)


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    合并所有重叠的区间。

    功能说明：
        - 给定一个区间数组，每个区间由一对整数表示其左端点和右端点，函数将所有重叠的区间合并为一个区间。

    算法思路：
        - 按照区间的左端点进行升序排序。这样可以确保处理区间时，可以按顺序逐个判断是否需要合并。
    """
    intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
    ans = []
    for p in intervals:
        if ans and p[0] <= ans[-1][1]:  # 可以合并
            ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
        else:  # 不相交，无法合并
            ans.append(p)  # 新的合并区间
    return ans


def huffman_tree_cost(stones: List[int]) -> int:
    """
    计算使用哈夫曼树合并算法的总代价。

    功能说明：
        - 给定一个整数列表，每个整数可以视为一个带权重的叶节点。
        - 哈夫曼树的构建过程中，每次选择两个权重最小的节点合并，生成一个新节点，其权重为两个子节点权重之和。
        - 合并的总代价等于每次合并生成的新节点的权重之和。
        - 此函数计算按照哈夫曼树合并策略从给定的节点列表构建完全二叉树所需要的总代价。
    """
    import heapq
    heapq.heapify(stones)
    total_cost = 0
    while len(stones) > 1:
        first_min = heapq.heappop(stones)
        second_min = heapq.heappop(stones)
        total_cost += first_min + second_min
        heapq.heappush(stones, first_min + second_min)
    return total_cost
