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
