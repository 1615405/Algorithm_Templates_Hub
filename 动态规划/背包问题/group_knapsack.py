def group_knapsack(max_capacity, groups_items):
    # 初始化动态规划数组，dp数组记录每个容量下可能达到的最大价值
    dp = [0] * (max_capacity + 1)

    # 遍历所有物品组
    for items in groups_items:
        # 逆向遍历背包容量，确保每个物品只被计算一次
        for current_capacity in range(max_capacity, -1, -1):
            # 遍历当前组中的每个物品
            for volume, value in items:
                if volume <= current_capacity:
                    dp[current_capacity] = max(dp[current_capacity], dp[current_capacity - volume] + value)

    # 返回最大容量下的最大价值
    return dp[max_capacity]


if __name__ == "__main__":
    num_groups, backpack_capacity = map(int, input().split())
    groups = []

    for _ in range(num_groups):
        num_items = int(input())
        current_group = []
        for _ in range(num_items):
            volume, value = map(int, input().split())
            current_group.append((volume, value))
        groups.append(current_group)

    max_value = group_knapsack(backpack_capacity, groups)
    print(max_value)