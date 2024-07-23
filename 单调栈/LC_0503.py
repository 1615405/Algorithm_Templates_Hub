class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(n * 2 - 1, -1, -1):
            x = nums[i % n]
            while stack and stack[-1] <= x:
                stack.pop()
            if stack and i < n:
                ans[i] = stack[-1]
            stack.append(x)
        
        return ans
