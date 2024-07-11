def longestCommonPrefix(strs: List[str]) -> str:
    """
    查找字符串数组中的最长公共前缀。

    参数：
        strs (List[str]): 输入的字符串数组。
    
    返回：
        str: 所有输入字符串的最长公共前缀。
    """
    lcp = 0
    for col in zip(*strs):  # zip(*strs)将字符串数组中相同位置的字符组成一个元组
        if len(set(col)) > 1:
            break
        lcp += 1
    
    return strs[0][:lcp]


def strStr(haystack: str, needle: str) -> int:
    """
    在字符串 haystack 中查找子字符串 needle 的第一个出现的位置。如果 needle 不是 haystack 的一部分，则返回 -1。

    参数：
        haystack (str): 待搜索的主字符串。
        needle (str): 需要搜索的子字符串。

    返回：
        int: 子字符串 needle 第一次出现的位置，如果未找到则返回 -1。
    
    方法：
        1. 如果 needle 的长度大于 haystack，直接返回 -1。
        2. 计算 needle 的哈希值。
        3. 通过滑动窗口计算 haystack 中每个子串的哈希值，比较哈希值以确定是否匹配。
    """
    if len(needle) > len(haystack):
        return -1
    
    def hash_function(s):
        import hashlib
        return hashlib.md5(s.encode()).hexdigest()
    
    needle_hash = hash_function(needle)
    
    for i in range(len(haystack) - len(needle) + 1):
        current_window = haystack[i:i+len(needle)]
        window_hash = hash_function(current_window)
        if window_hash == needle_hash:
            return i
    
    return -1
