class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        rank = defaultdict(int)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                rank[stack.pop()] = i
            stack.append(i)
        
        while stack:
            idx = stack.pop()
            rank[idx] = idx
        
        return [rank[i] - i for i, _ in enumerate(temperatures)]
