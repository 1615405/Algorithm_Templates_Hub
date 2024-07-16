# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    判断两棵二叉树是否相同。如果两棵树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

    参数：
        p (Optional[TreeNode]): 第一棵树的根节点。
        q (Optional[TreeNode]): 第二棵树的根节点。
    
    返回：
        bool: 如果两棵树相同，则返回 True，否则返回 False。
    """
    if not p or not q:
        return p is q

    if p.val != q.val:
        return False
        
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    翻转一棵二叉树。每个节点的左右子树会被交换。

    参数:
        root (Optional[TreeNode]): 二叉树的根节点。

    返回:
        Optional[TreeNode]: 翻转后的二叉树的根节点。
    """
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def isBalanced(root: Optional[TreeNode]) -> bool:
    """
    判断一棵二叉树是否是高度平衡的。高度平衡的二叉树是指任何一个节点的两个子树的高度差不超过1。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        bool: 如果二叉树是高度平衡的，则返回True；否则返回False。
    """
    def height(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(height(root.left), height(root.right)) + 1
    
    if not root:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    判断一个二叉树是否是另一个二叉树的子树。
    
    参数:
        root (TreeNode, 可选): 主树的根节点。
        subRoot (TreeNode, 可选): 子树的根节点。

    返回:
        bool: 如果 subRoot 是 root 的子树，返回 True，否则返回 False。
    """
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:  return p is q
        if p.val != q.val:  return False
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    
    if not root or not subRoot:
        return root is subRoot
    return isSameTree(root, subRoot) or isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def mergeTrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    合并两棵二叉树，每个对应节点的值相加，如果一个位置只有一个树有节点，则直接使用该节点。

    参数:
        root1 (TreeNode, 可选): 第一棵二叉树的根节点。
        root2 (TreeNode, 可选): 第二棵二叉树的根节点。

    返回:
        TreeNode, 可选: 合并后的二叉树的根节点，如果两棵树均为空，则返回 None。
    """
    if not root1:  return root2
    if not root2:  return root1
    
    return TreeNode(root1.val + root2.val,
        mergeTrees(root1.left, root2.left),
        mergeTrees(root1.right, root2.right))
