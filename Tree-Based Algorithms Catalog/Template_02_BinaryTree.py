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


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    在二叉搜索树中搜索给定值的节点。如果存在这样的节点，则返回该节点；否则返回 None。

    参数:
        root (TreeNode, 可选): 二叉搜索树的根节点。
        val (int): 需要搜索的节点值。

    返回:
        TreeNode, 可选: 包含给定值的节点，如果没有找到则返回 None。
    """
    if not root:
        return None
        
    if root.val == val:
        return root
        
    return searchBST(root.left if val < root.val else root.right, val)


def minDepth(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的最小深度。最小深度是从根节点到最近叶子节点的最短路径上的节点数。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        int: 二叉树的最小深度。
    """
    if root is None:
        return 0
        
    if root.right is None:
        return minDepth(root.left) + 1
        
    if root.left is None:
        return minDepth(root.right) + 1
        
    return min(minDepth(root.left), minDepth(root.right)) + 1


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    判断二叉树中是否存在一条路径，该路径上的节点值之和等于给定的目标值 targetSum。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
        targetSum (int): 路径和的目标值。
    
    返回：
        bool: 如果存在这样的路径，则返回 True；否则返回 False。
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        isLeafNode = lambda node: not node.left and not node.right
        
        if not root:  return False
            
        if isLeafNode(root):
            return targetSum == root.val
            
        return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    """
    将一个按升序排列的整数数组转换为一棵高度平衡的二叉搜索树。高度平衡的二叉树是指每个节点的两个子树的深度差不超过1。
    
    参数：
        nums (List[int]): 升序排列的整数数组。
    
    返回：
        Optional[TreeNode]: 高度平衡二叉搜索树的根节点。
    """
    def helper(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid - 1)
        root.right = helper(mid + 1, right)
        return root
    
    return helper(0, len(nums) - 1)
