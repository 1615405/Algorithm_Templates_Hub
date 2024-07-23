class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def dfs(x: int, y: int) -> int:
            if x <= y:  return y - x
            return min(x - y,
                    dfs(x // 11, y) + x % 11 + 1,
                    dfs(x // 11 + 1, y) + 11 - x % 11 + 1,
                    dfs(x // 5, y) + x % 5 + 1,
                    dfs(x // 5 + 1, y) + 5 - x % 5 + 1
                )
        
        return dfs(x, y)
