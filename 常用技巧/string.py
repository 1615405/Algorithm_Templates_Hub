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