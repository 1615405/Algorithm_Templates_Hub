class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for i in range(1024):
            hour, minute = i >> 6, i & 0x3f
            if hour < 12 and minute < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{hour}:{minute:02d}")
        return ans