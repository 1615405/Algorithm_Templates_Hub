# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    对二叉树进行先序遍历（根-左-右）并返回遍历的结果。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        List[int]: 存储先序遍历结果的列表。
    """
    if not root: return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    对二叉树进行中序遍历并返回遍历结果的列表。中序遍历首先访问左子树，然后访问根节点，最后访问右子树。

    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        List[int]: 中序遍历的节点值构成的列表。
    """
    if not root: return []
    res, stack = [], []
    while root:
        if root.left:
            stack.append(root)
            root = root.left
        else:
            while stack and not root.right:
                res.append(root.val)
                root = stack.pop()
            res.append(root.val)
            root = root.right
    return res


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    对二叉树进行后序遍历（左-右-根）并返回遍历的结果。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        List[int]: 存储后序遍历结果的列表。
    """
    if not root: return []
    res, stack = [], [root]
    prev = root
    while stack:
        root = stack.pop()
        if (not root.left and not root.right) or (root.left == prev or root.right == prev):
            prev = root
        else:
            stack.append(root)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
    return res


def averageOfLevels(root: Optional[TreeNode]) -> List[float]:
    """
    计算二叉树每一层的平均值。

    参数:
        root (TreeNode, 可选): 二叉树的根节点。

    返回:
        List[float]: 包含每一层节点平均值的列表。如果树为空，返回空列表。
    """
    averages = list()
    queue = collections.deque([root])
    while queue:
        total = 0
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            total += node.val
            left, right = node.left, node.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        averages.append(total / size)
    return averages
