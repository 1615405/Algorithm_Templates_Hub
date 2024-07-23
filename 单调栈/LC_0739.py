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


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        rank = defaultdict(int)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            rank[i] = stack[-1] if stack else i
            stack.append(i)
        return [rank[i] - i for i in range(len(temperatures))]
