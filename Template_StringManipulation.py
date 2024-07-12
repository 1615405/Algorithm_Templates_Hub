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


def isIsomorphic(s: str, t: str) -> bool:
    """
    判断两个字符串 s 和 t 是否是同构的。同构字符串的定义是：字符串 s 可以通过替换字符的方式转换为字符串 t。
    要求每个字符的替换是一致的，且一个字符只能替换为一个字符（不允许多对一或一对多的映射）。

    参数：
        s (str): 第一个字符串。
        t (str): 第二个字符串。
    
    返回：
        bool: 如果 s 和 t 是同构的，则返回 True，否则返回 False。
    """
    s2t, t2s = {}, {}
    for a, b in zip(s, t):
        if s2t.get(a, b) != b or t2s.get(b, a) != a:
            return False
        s2t[a], t2s[b] = b, a
    return True


def isAnagram(s: str, t: str) -> bool:
    """
    判断两个字符串是否互为异位词。异位词指的是两个字符串拥有相同的字符和相同的字符频次，但字符顺序可以不同。

    参数:
        s (str): 第一个字符串。
        t (str): 第二个字符串。

    返回:
        bool: 如果两个字符串是变位词则返回 True，否则返回 False。
    """
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1
    for c in t:
        cnt[ord(c) - ord('a')] -= 1
    return all(c == 0 for c in cnt)
