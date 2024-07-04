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



def longestPalindrome(s: str) -> str:
    """
    寻找并返回字符串中的最长回文子串。

    说明:
    - 使用中心扩展算法来查找每个可能的回文中心，并扩展直到回文不再成立。
    - 对于每个字符，考虑它自己作为中心（奇数长度的回文）和它及其右侧字符作为中心（偶数长度的回文）。
    - 更新记录最长回文的起始和结束位置。
    """
    def expandAroundCenter(left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(i, i)
        left2, right2 = expandAroundCenter(i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start: end + 1]



def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    将字符串数组按照字母异位词分组。

    说明:
    - 字母异位词是指由相同的字符以不同顺序构成的词。
    - 通过对字符串数组中的每个元素进行排序，并使用排序后的结果作为键存储到哈希表中，
        这样所有的异位词都将映射到相同的键。
    - 使用 defaultdict(list) 来收集每个键对应的所有字符串，最后返回这个字典的值。
    """
    anagrams = defaultdict(list)  # 创建一个默认字典，值类型为list
    for word in strs:
        sorted_word = tuple(sorted(word))  # 对单词进行排序并转换为元组作为字典键
        anagrams[sorted_word].append(word)  # 将原始单词添加到对应的列表中
    
    return list(anagrams.values())  # 返回字典中所有值的列表



def validPalindrome(self, s: str) -> bool:
    """
    判断给定字符串是否可以通过删除最多一个字符变成回文。

    说明:
    - 使用双指针技术从字符串两端向中心移动。
    - 当发现不匹配的字符时，检查两种可能的情况：
        1. 删除左边的字符后，剩余部分是否为回文。
        2. 删除右边的字符后，剩余部分是否为回文。
    - 如果其中任何一种情况使得剩余部分为回文，则整体字符串可视为可通过删除一个字符成为回文的字符串。
    """
    def checkPalindrome(low: int, high: int) -> bool:
        """ 辅助函数，用于检查s[low:high+1]是否为回文。 """
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return False
        return True

    n = len(s)
    left, right = 0, n - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return checkPalindrome(left + 1, right) or checkPalindrome(left, right - 1)
    return True