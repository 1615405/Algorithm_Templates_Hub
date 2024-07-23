class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []

        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                bottom_h = height[stack.pop()]
                if not stack:
                    break
                left = stack[-1]
                dh = min(h, height[left]) - bottom_h
                ans += (i - left - 1) * dh
            stack.append(i)
        
        return ans
