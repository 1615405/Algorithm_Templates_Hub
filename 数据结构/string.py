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