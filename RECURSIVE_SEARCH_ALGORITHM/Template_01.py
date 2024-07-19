def readBinaryWatch(turnedOn: int) -> List[str]:
    """
    计算所有可能的时间，其中二进制表示中有指定数量的 1s 的灯被点亮。
    """
    ans = list()
    for i in range(1024):  # 1024 = 2^10，因为总共有 10 个灯（4 个小时灯，6 个分钟灯）
        h, m = i >> 6, i & 0x3f  # 提取小时数和分钟数
        if h < 12 and m < 60 and bin(i).count("1") == turnedOn:  # 验证时间的有效性和点亮灯的数量
            ans.append(f"{h}:{m:02d}")  # 格式化输出并添加到结果列表
    return ans