class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dfs(n: int) -> int:
            if n <= 1:  return n
            return min(dfs(n // 2) + n % 2, dfs(n // 3) + n % 3) + 1
        
        return dfs(n)