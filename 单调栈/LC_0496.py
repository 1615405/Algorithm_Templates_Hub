class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, next_greater = list(), defaultdict(int)
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[num] for num in nums1]


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, next_greater = list(), defaultdict(int)
        for num in reversed(nums2):
            # 比当前元素大的前一个元素(历史元素中)
            while stack and stack[-1] <= num:
                stack.pop()
            next_greater[num] = stack[-1] if stack else -1
            stack.append(num)
        return [next_greater[num] for num in nums1]
