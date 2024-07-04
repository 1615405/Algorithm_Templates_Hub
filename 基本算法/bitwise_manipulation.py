def lowbit(x: int) -> int:
    """
    获取整数 x 的二进制表示中最低位的1及其后面的所有0。
    """
    return x & -x



def hammingWeight(n: int) -> int:
    """
    计算一个无符号整数的二进制表示中1的个数。
    """
    ret = 0
    while n:
        n = n & (n - 1)
        ret += 1
    return ret



def isPowerOfTwo(n: int) -> bool:
    """
    判断一个整数是否是2的幂。
    """
    if n <= 0:
        return False
    
    return (n & (n - 1)) == 0



def isPowerOfFour(n: int) -> bool:
    """
    判断一个整数是否是4的幂。
    """
    # 0xAAAAAAAA 是一个32位整数，其中偶数位置上的位都是1，奇数位置上的位都是0
    NOT_FOUR_POWER_MASK = 0xAAAAAAAA
    
    # n 必须大于 0
    if n <= 0:
        return False

    # n 必须是 2 的幂
    if n & (n - 1) != 0:
        return False

    # n 的 1 必须在 4 的幂的位置，即1的位置必须在奇数位上
    return (n & NOT_FOUR_POWER_MASK) == 0



def hasAlternatingBits(self, n: int) -> bool:
    """
    检查一个整数的二进制表示是否由交替的0和1组成。
    """
    xor_n = n ^ (n >> 1)  # 创建一个全1的模式如果 n 是交替的

    # 检查 xor_n 是否全为1
    return xor_n & (xor_n + 1) == 0



def reverseBits(n: int) -> int:
    """
    反转一个给定的 32 位无符号整数的比特位。
    """
    M1 = 0x55555555  # 01010101010101010101010101010101
    M2 = 0x33333333  # 00110011001100110011001100110011
    M4 = 0x0f0f0f0f  # 00001111000011110000111100001111
    M8 = 0x00ff00ff  # 00000000111111110000000011111111

    # 交换奇偶位
    n = (n >> 1 & M1) | ((n & M1) << 1)
    # 交换连续对
    n = (n >> 2 & M2) | ((n & M2) << 2)
    # 交换四位组
    n = (n >> 4 & M4) | ((n & M4) << 4)
    # 交换字节
    n = (n >> 8 & M8) | ((n & M8) << 8)
    # 交换两字节长的对
    n = (n >> 16) | (n << 16) & 0xFFFFFFFF  # 确保 n 被当作 32 位处理

    return n