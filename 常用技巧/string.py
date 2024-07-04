def is_isomorphic(s: str, t: str) -> bool:
    """
    检查两个字符串是否是同构的。
    """
    s2t, t2s = {}, {}  # s到t和t到s的映射字典

    for char_s, char_t in zip(s, t):
        if s2t.get(char_s, char_t) != char_t or t2s.get(char_t, char_s) != char_s:
            return False
        s2t[char_s], t2s[char_t] = char_t, char_s

    return True



def str_str(haystack: str, needle: str) -> int:
    """
    在 haystack 字符串中查找 needle 字符串的第一个出现的位置。使用哈希匹配以优化搜索效率。
    """
    # 如果 needle 为空字符串，根据约定返回 0
    if not needle:
        return 0
    
    # 如果 needle 长度大于 haystack，无法匹配，返回 -1
    if len(needle) > len(haystack):
        return -1

    # 定义哈希函数，这里使用 md5
    def hash_function(s: str) -> str:
        import hashlib
        return hashlib.md5(s.encode()).hexdigest()
    
    # 计算 needle 的哈希值
    needle_hash = hash_function(needle)
    
    # 滑动窗口遍历 haystack 来查找匹配的哈希值
    for i in range(len(haystack) - len(needle) + 1):
        current_window = haystack[i:i+len(needle)]
        window_hash = hash_function(current_window)
        
        if window_hash == needle_hash:
            # 如果哈希值匹配，返回当前索引
            return i
    
    # 如果遍历完成没有找到匹配，返回 -1
    return -1



def longestCommonPrefix(strs: List[str]) -> str:
    """
    寻找字符串数组中的最长公共前缀。
    """
    lcp = 0  # 最长公共前缀的长度初始化为0
    for col in zip(*strs):  # 使用 zip 来并行迭代每个字符串的相同位置的字符
        if len(set(col)) > 1:  # 如果当前列的字符不全相同
            break  # 结束循环
        lcp += 1  # 如果当前列的字符全相同，公共前缀长度加1
    
    return strs[0][:lcp]  # 返回第一个字符串的前 lcp 个字符作为最长公共前缀



def gcdOfStrings(str1: str, str2: str) -> str:
    """
    计算两个字符串的最大公共除数字符串。
    """
    # 判断两个字符串的拼接是否相等
    if str1 + str2 != str2 + str1:
        return ""
    
    # 求两个数的最大公因数
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    # 求两个字符串长度的最大公因数
    gcd_length = gcd(len(str1), len(str2))
    
    # 截取任意一个字符串的前 gcd_length 个字符
    return str1[:gcd_length]