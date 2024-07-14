def reverseBits(n: int) -> int:
    """
    反转一个 32 位无符号整数的二进制位。

    参数：
        n (int): 一个无符号整数，表示为 32 位。
    
    返回：
        int: 二进制位反转后的整数。
    """
    M1 = 0x55555555  # 01010101010101010101010101010101
    M2 = 0x33333333  # 00110011001100110011001100110011
    M4 = 0x0f0f0f0f  # 00001111000011110000111100001111
    M8 = 0x00ff00ff  # 00000000111111110000000011111111

    n = (n >> 1 & M1) | ((n & M1) << 1)
    n = (n >> 2 & M2) | ((n & M2) << 2)
    n = (n >> 4 & M4) | ((n & M4) << 4)
    n = (n >> 8 & M8) | ((n & M8) << 8)
    n = (n >> 16) | (n << 16) & 0xFFFFFFFF  # Ensure n is treated as 32 bits

    return n


def hammingWeight(n: int) -> int:
    """
    计算一个无符号整数的二进制表示中数字位为 '1' 的数量。

    参数：
        n (int): 一个无符号整数。

    返回：
        int: 输入整数的二进制表示中 '1' 的个数。
    """
    ret = 0
    while n:
        n = n & (n - 1)
        ret += 1
    return ret


def isPowerOfTwo(n: int) -> bool:
    """
    判断给定的整数 n 是否是 2 的幂次方。2 的幂次方在二进制表示中有且仅有一个 1，通过 n 和 n-1 的位与操作来确定。

    参数:
        n (int): 需要判断的整数。

    返回:
        bool: 如果 n 是 2 的幂次方则返回 True，否则返回 False。
    """
    if n <= 0:
        return False
    return (n & (n -1)) == 0


def isPowerOfFour(n: int) -> bool:
    """
    判断给定的整数 n 是否是 4 的幂次方。

    参数:
        n (int): 需要判断的整数。

    返回:
        bool: 如果 n 是 4 的幂次方则返回 True，否则返回 False。
    """
    NOT_FOUR_POWER_MASK = 0xAAAAAAAA
    if n <= 0:  
        return False

    if n & (n - 1) != 0:  
        return False

    return (n & NOT_FOUR_POWER_MASK) == 0


def findComplement(num: int) -> int:
     """
    计算给定整数的二进制补码。二进制补码是将二进制数中的每一位取反（1变0，0变1）后的结果。

    参数:
        num (int): 需要求补码的正整数。

    返回:
        int: 输入整数的二进制补码。
    """
    highbit = num.bit_length()
    mask = (1 << (highbit)) - 1
    return num ^ mask


def hasAlternatingBits(n: int) -> bool:
    """
    检查整数的二进制表示是否由交替的 0 和 1 位组成。

    参数:
        n (int): 需要检查的整数。

    返回:
        bool: 如果整数的二进制位交替为 0 和 1，则返回 True，否则返回 False。
    """
    xor_n = n ^ (n >> 1)
    return xor_n & (xor_n + 1) == 0
