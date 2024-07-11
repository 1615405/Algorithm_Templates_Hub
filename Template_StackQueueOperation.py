def isValid(s: str) -> bool:
    """
    检查输入的字符串 s 是否为有效的括号组合。

    参数：
        s (str): 待检查的字符串，包含 '(', ')', '[', ']', '{', '}' 六种字符。

    返回：
        bool: 如果字符串为有效的括号组合，则返回 True, 否则返回 False。
    """
    stack = []
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for char in s:
        if char in pairs:  # 如果是开括号，推入栈中
            stack.append(char)
        else:
            if not stack or char != pairs[stack[-1]]:  # 如果栈为空或者栈顶括号不匹配当前闭括号
                return False
            stack.pop()  # 匹配成功，弹出栈顶括号

    return len(stack) == 0  # 栈为空表示所有括号都匹配成功
