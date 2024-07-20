class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i <= 1:
                return 0
            return min(dfs(i - 2) + cost[i - 2], dfs(i - 1) + cost[i - 1])
        
        return dfs(len(cost))