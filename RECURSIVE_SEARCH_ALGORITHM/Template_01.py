def readBinaryWatch(turnedOn: int) -> List[str]:
    """
    计算所有可能的时间，其中二进制表示中有指定数量的 1s 的灯被点亮。
    """
    ans = list()
    for i in range(1024):
        hour, minute = i >> 6, i & 0x3f
        if hour < 12 and minute < 60 and bin(i).count("1") == turnedOn:
            ans.append(f"{hour}:{minute:02d}")
    return ans
