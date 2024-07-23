class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = list()
        left = [0] * n
        right = [0] * n

        for i, x in enumerate(heights):
            while stack and heights[stack[-1]] >= x:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        ans = 0
        for x, l, r in zip(heights, left, right):
            ans = max(ans, (r - l - 1) * x)
        return ans
