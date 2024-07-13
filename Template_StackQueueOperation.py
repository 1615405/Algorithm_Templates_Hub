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


class MyStack:
    """
    使用单个队列实现栈的数据结构。栈是一种后进先出（LIFO）的数据结构，只允许在栈顶进行添加和删除操作。
    """
    def __init__(self):
        from collections import deque
        self.queue = deque()

    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


class MyQueue:
    """
    使用两个栈实现一个队列。队列是一种先进先出（FIFO）的数据结构，元素从队列的一端添加，从另一端移除。
    """
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        peek = self.peek()
        self.B.pop()
        return peek

    def peek(self) -> int:
        if self.B:  return self.B[-1]
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self) -> bool:
        return not self.A and not self.B


def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    在数组 nums2 中寻找数组 nums1 的每个元素的下一个更大元素。

    参数:
        nums1 (List[int]): 第一个列表，包含需要查找下一个更大元素的目标元素。
        nums2 (List[int]): 第二个列表，其中包含 nums1 的所有元素，并且可能包含更多元素。

    返回:
        List[int]: 一个列表，表示 nums1 中每个元素在 nums2 中的下一个更大元素的值。

    描述:
    使用单调栈和哈希表的组合来优化搜索过程。首先反向遍历 nums2，使用栈来存储未来可能的更大元素。
    对于 nums2 中的每个元素，如果它比栈顶元素小或栈为空，则直接将其加入栈中；
    如果它比栈顶元素大，则弹出栈顶元素，直到找到一个更大的元素或栈为空。使用哈希表记录每个元素的下一个更大元素。
    """
    res = defaultdict(int)
    stack = []
    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()
        res[num] = stack[-1] if stack else -1
        stack.append(num)
    return [res[num] for num in nums1]
