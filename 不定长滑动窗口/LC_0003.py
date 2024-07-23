class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        cnt = defaultdict(int)

        for right, char in enumerate(s):
            cnt[char] += 1
            while left <= right and cnt[char] >= 2:
                cnt[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        
        return max_length
