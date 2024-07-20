class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)

        @cache
        def can_decode(start: int) -> bool:
            if start == n - 1:
                return bits[start] == 0
            if start >= n:
                return False
            if bits[start] == 0:
                return can_decode(start + 1)
            if start + 1 < n and bits[start] == 1:
                return can_decode(start + 2)
        return can_decode(0)