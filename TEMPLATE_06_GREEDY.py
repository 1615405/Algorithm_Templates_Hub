# ****************** 区间合并问题 ******************
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    将给定的区间列表合并，返回不重叠的区间列表。
    参数:
        intervals: 二维列表，每个子列表表示一个区间，形如[start, end]
    返回:
        合并后的区间列表
    """
    intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
    ans = []
    for p in intervals:
        if ans and p[0] <= ans[-1][1]:  # 可以合并
            ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
        else:  # 不相交，无法合并
            ans.append(p)  # 新的合并区间
    return ans
# **************************************************



# ****************** 最大不重叠区间及区间选点问题 ******************
def max_non_overlapping_intervals(intervals):
    """
    给定一系列闭区间，此函数计算最大不重叠区间数量，
    并可用于确定覆盖所有给定区间的最少点数。
    参数:
        intervals: 二维列表，每个子列表表示一个区间，形如[start, end]
    返回:
        最大不重叠区间的数量，也是覆盖所有区间的最少点数
    """
    # 按照区间的结束时间排序
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_end = float('-inf')

    # 遍历所有区间
    for start, end in intervals:
        # 如果当前区间的开始时间大于上一个选中区间的结束时间
        if start > last_end:
            # 选择当前区间的结束点作为覆盖点
            count += 1
            last_end = end  # 更新最后一个选中区间的结束时间

    return count
# ***************************************************************



# ****************** 区间分组问题 ******************
def min_interval_groups(intervals):
    """
    给定一系列可能重叠的区间，计算需要最少的不重叠组数。
    参数:
        intervals: 二维列表，每个子列表表示一个区间，形如[start, end]
    返回:
        最少的不重叠组数
    """
    # 对区间按起始时间进行排序
    intervals.sort()

    # 使用堆（优先队列）来跟踪每个组的最小结束时间
    import heapq
    heap = []

    # 遍历所有区间
    for interval in intervals:
        # 如果堆不为空且堆顶元素（最早结束的组的结束时间）小于当前区间的起始时间
        if heap and heap[0] < interval[0]:
            # 替换堆顶元素，相当于将当前区间加入该组，并更新该组的结束时间
            heapq.heapreplace(heap, interval[1])
        else:
            # 否则，创建一个新的组
            heapq.heappush(heap, interval[1])

    # 堆的大小就是所需的最少组数
    return len(heap)
# **************************************************



# ****************** 区间覆盖问题 ******************
def min_intervals_to_cover_segment(s, t, intervals):
    """
    计算覆盖从 s 到 t 的线段所需的最少区间数量。
    参数:
        s: 线段的起始点
        t: 线段的结束点
        intervals: 二维列表，每个子列表表示一个区间，形如[start, end]
    返回:
        覆盖整个线段所需的最少区间数量；如果无法覆盖，返回 -1
    """
    # 特殊情况处理，当 s 和 t 相等时
    if s == t:
        for a, b in intervals:
            if a <= s <= b:
                return 1
        return -1  # 如果没有任何区间包含点 s，返回 -1

    # 过滤无关区间并按起始点升序排序，起始相同按结束点降序排序
    intervals = [x for x in intervals if x[0] <= t and x[1] >= s]
    intervals.sort(key=lambda x: (x[0], -x[1]))

    # 初始化
    count = 0
    current_end = s
    index = 0
    max_end = s

    while current_end < t:
        found = False
        # 在当前可选的区间中找到最远的区间
        while index < len(intervals) and intervals[index][0] <= current_end:
            max_end = max(max_end, intervals[index][1])
            found = True
            index += 1
        
        if not found:
            return -1  # 如果找不到可用区间，则无法覆盖
        
        current_end = max_end
        count += 1

        if current_end >= t:
            break

    return count
# **************************************************



# ****************** 霍夫曼树成本计算 ******************
def huffman_tree_cost(numbers):
    """
    计算给定数字列表构建霍夫曼树的总成本。
    参数:
        numbers: 整数列表，每个整数代表一个节点的权重
    返回:
        构建霍夫曼树的总成本
    """
    import heapq
    heapq.heapify(numbers)
    
    total_cost = 0
    while len(numbers) > 1:
        first_min = heapq.heappop(numbers)
        second_min = heapq.heappop(numbers)
        total_cost += first_min + second_min
        heapq.heappush(numbers, first_min + second_min)
    
    return total_cost
# **************************************************



# ****************** 最小化总等待时间 ******************
def minimize_total_wait(times):
    """
    根据给定的处理时间列表，计算并返回按最优顺序执行时的最小总等待时间。
    参数:
        times: 整数列表，表示每个任务的处理时间
    返回:
        执行所有任务的最小总等待时间
    """
    times.sort()
    total_waiting_time = 0
    current_wait = 0

    for time in times:
        total_waiting_time += current_wait
        current_wait += time

    return total_waiting_time
# **************************************************



# ****************** 最优仓库位置计算 ******************
def optimal_warehouse_location(shops):
    """
    计算给定商店位置的最优仓库位置以最小化到所有商店的总距离。
    参数:
        shops: 整数列表，表示每个商店的位置
    返回:
        最小化到所有商店的总距离
    """
    shops.sort()
    total_distance = 0
    for i in range(len(shops)):
        total_distance += shops[i] - shops[i >> 1]
    
    return total_distance
# *****************************************************



# ****************** 最小化堆叠风险评估 ******************
def minimize_stack_risk(items):
    """
    此函数计算在堆叠具有不同重量和强度的物品时的最小可能风险。通过贪心算法排序（按每个物品的重量加强度的总和），
    我们可以确保在每个物品上堆叠时的风险最小化，从而达到全局的最小风险。

    参数:
        items: 元组列表，每个元组表示一个物品，形式为(weight, strength)
    返回:
        所有物品按最优顺序堆叠后可能出现的最大风险的最小值
    """
    # 计算每个物品的总承载能力（重量 + 强度）并排序
    items = [(weight + strength, weight) for weight, strength in items]
    items.sort()

    max_risk = -float('inf')
    total_weight = 0

    for total, weight in items:
        strength = total - weight
        risk = total_weight - strength
        max_risk = max(max_risk, risk)
        total_weight += weight

    return max_risk
# **************************************************