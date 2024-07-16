# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    """
    计算给定二叉树中所有左叶子节点的值之和。

    参数:
        root (Optional[TreeNode]): 二叉树的根节点。

    返回:
        int: 所有左叶子节点的值之和。
    """
    isLeafNode = lambda node: not node.left and not node.right
    def dfs(node: Optional[TreeNode]) -> int:
        ans = 0
        if node.left:
            ans += node.left.val if isLeafNode(node.left) else dfs(node.left)
        if node.right and not isLeafNode(node.right):
            ans += dfs(node.right)
        return ans
    return dfs(root) if root else 0


def findMode(root: Optional[TreeNode]) -> List[int]:
    """
    查找二叉搜索树中的众数(出现频率最高的元素)。

    参数:
        root (TreeNode, 可选): 二叉搜索树的根节点。

    返回:
        List[int]: 包含所有众数的列表。
    """
    result = []
    maxFreq = 0
    cur = None
    freq = 0

    def dfs(node):
        nonlocal cur, maxFreq, result, freq
        if not node: return
        dfs(node.left)
        if cur == node.val:
            freq += 1
        else:
            freq = 1
            cur = node.val
        if freq == maxFreq:
            result.append(cur)
        elif freq > maxFreq:
            result = [cur]
            maxFreq = freq
        dfs(node.right)
    dfs(root)
    return result


def getMinimumDifference(root: Optional[TreeNode]) -> int:
    """
    计算给定二叉搜索树中任意两个节点值的最小差异。

    参数:
        root (TreeNode, 可选): 二叉搜索树的根节点。

    返回:
        int: 最小差异的数值。
    """
    stack = []
    result = float('inf')
    previous = None
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            current = stack.pop()
            if previous:  result = min(current.val - previous.val, result)
            previous = current
            root = current.right
    return result


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的直径，即二叉树中任意两个节点之间的最长路径的边数。
    
    参数:
        root (TreeNode, 可选): 二叉树的根节点。

    返回:
        int: 二叉树的直径。
    """
    ans = 0
    def dfs(node: Optional[TreeNode]) -> int:
        if node is None:
            return -1
        l_len = dfs(node.left) + 1
        r_len = dfs(node.right) + 1
        nonlocal ans
        ans = max(ans, l_len + r_len)
        return max(l_len, r_len)
    dfs(root)
    return ans


def findTilt(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的所有节点的倾斜度总和。节点的倾斜度定义为该节点的左子树节点值之和与右子树节点值之和的绝对差。
    
    参数:
        root (TreeNode, 可选): 二叉树的根节点。
    
    返回:
        int: 所有节点的倾斜度之和。
    """
    ans = 0
    def dfs(root: Optional[TreeNode]) -> int:
        if not root:  return 0
        sum_left = dfs(root.left)
        sum_right = dfs(root.right)
        nonlocal ans
        ans += abs(sum_left - sum_right)
        return sum_left + sum_right + root.val
    dfs(root)
    return ans


def countNodes(root: Optional[TreeNode]) -> int:
    """
    计算完全二叉树中的节点数。利用二分查找结合位操作，以优化性能，避免直接的完全遍历。

    参数：
        root (Optional[TreeNode]): 完全二叉树的根节点。

    返回：
        int: 树中的节点总数。
    """
    def exists(root: Optional[TreeNode], level: int, k: int) -> bool:
        bits = 1 << (level - 1)
        while root and bits > 0:
            if (bits & k) == 0:
                root = root.left
            else:
                root = root.right
            bits >>= 1
        return root is not None
    
    if not root:  return 0

    level = 0
    node = root
    while node.left:
        level += 1
        node = node.left
    
    low, high = 1 << level, (1 << (level + 1)) - 1
    while low < high:
        mid = (low + high + 1) // 2
        if exists(root, level, mid):
            low = mid
        else:
            high = mid - 1
    return low