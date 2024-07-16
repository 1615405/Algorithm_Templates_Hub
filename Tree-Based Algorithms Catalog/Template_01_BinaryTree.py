# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    对二叉树进行先序遍历（根-左-右）并返回遍历的结果。
    """
    if not root:  return []
    result, stack = [], []
    while stack or root:
        while root:
            result.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return result


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    中序遍历首先访问左子树，然后访问根节点，最后访问右子树。
    """
    current, result, stack = root, [], []
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    对二叉树进行后序遍历（左-右-根）并返回遍历的结果。
    """
    if not root:  return []
    prev, result, stack = None, [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            result.append(root.val)
            prev = root
            root = None
        else:
            stack.append(root)
            root = root.right
    return result


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    进行二叉树的层序遍历并返回节点值的分层列表。
    """
    if not root:  return []
    ans, queue = [], collections.deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(level)
    return ans


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    判断两棵二叉树是否相同。如果两棵树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
    """
    if p is None or q is None:
        return p is q
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isBalanced(root: Optional[TreeNode]) -> bool:
    """
    判断一棵二叉树是否是高度平衡的。高度平衡的二叉树是指任何一个节点的两个子树的高度差不超过1。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        bool: 如果二叉树是高度平衡的，则返回True；否则返回False。
    """
    def height(root: Optional[TreeNode]) -> int:
        if not root:  return 0
        return max(height(root.left), height(root.right)) + 1
    
    if not root:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    """
    计算给定二叉树中所有左叶子节点的值之和。
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
