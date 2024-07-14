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
    res, stack = [], [root] # 利用栈进行临时存储
    while stack:
        node = stack.pop() # 取出一个节点，表示开始访问以该节点为根的子树
        res.append(node.val) # 首先访问该节点（先序），之后顺序入栈右子树，左子树
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
        if root.left: # 存在左子树，入栈并深入左子树
            stack.append(root)
            root = root.left
        else: # 否则就可以寻找深入右子树的节点
            while stack and not root.right: # 对于不能深入右子树的节点，直接访问，此时子树访问结束
                res.append(root.val)
                root = stack.pop()
            res.append(root.val) # 如果可以深入右子树，访问该节点后，深入右子树
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
    prev = root # 为了判断父子节点关系
    while stack:
        root = stack.pop() # 取出一个节点，表示开始访问以该节点为根的子树
        if (not root.left and not root.right) or (root.left == prev or root.right == prev): # 如果该节点为叶子节点，或者已经访问该节点的子节点
            res.append(root.val) # 直接访问
            prev = root
        else: # 否则就顺序把当前节点，右孩子，左孩子入栈
            stack.append(root)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
    return res


def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    """
    生成从根节点到每个叶子节点的所有路径的字符串表示。
    
    参数:
        root (Optional[TreeNode]): 二叉树的根节点。

    返回:
        List[str]: 包含每个从根到叶路径的字符串列表，每个路径的格式如 "1->2->3"。
    """
    def construct_paths(root, path):
        if not root:  return None
        path += str(root.val)
        if not root.left and not root.right:  # 当前节点是叶子节点
            paths.append(path)  # 把路径加入到答案中
        else:
            path += '->'  # 当前节点不是叶子节点，继续递归遍历
            construct_paths(root.left, path)
            construct_paths(root.right, path)

    paths = []
    construct_paths(root, '')
    return paths


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


def isSymmetric(root: Optional[TreeNode]) -> bool:
    """
    检查给定的二叉树是否是对称的。

    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        bool: 如果树是对称的，则返回 True，否则返回 False。
    """
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)
    
    return isSameTree(root, root)


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    翻转一棵二叉树。每个节点的左右子树会被交换。

    参数:
        root (Optional[TreeNode]): 二叉树的根节点。

    返回:
        Optional[TreeNode]: 翻转后的二叉树的根节点。
    """
    if not root:  return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    计算二叉树的最大深度。最大深度是从根节点到最远叶子节点的最长路径上的节点数。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
    
    返回：
        int: 二叉树的最大深度。
    """
    if root is None: return 0
    l_depth = maxDepth(root.left)
    r_depth = maxDepth(root.right)
    return max(l_depth, r_depth) + 1  # 返回最大深度加一（根节点）


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


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    """
    判断二叉树中是否存在一条路径，该路径上的节点值之和等于给定的目标值 targetSum。
    
    参数：
        root (Optional[TreeNode]): 二叉树的根节点。
        targetSum (int): 路径和的目标值。
    
    返回：
        bool: 如果存在这样的路径，则返回 True；否则返回 False。
    """
    if not root:
        return False

    if root.left is root.right:
        return targetSum == root.val
    
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)


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


def findTarget(root: Optional[TreeNode], k: int) -> bool:
    """
    判断二叉树中是否存在两个节点，使得这两个节点的值之和等于给定的数 k。

    参数:
        root (TreeNode, 可选): 二叉树的根节点。
        k (int): 需要查找的目标和。

    返回:
        bool: 如果存在两个节点的值之和等于 k，则返回 True；否则返回 False。
    """
    seen = set()
    def helper(node, k):
        nonlocal seen
        if node is None:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return helper(node.left, k) or helper(node.right, k)
    return helper(root, k)


def findSecondMinimumValue(root: Optional[TreeNode]) -> int:
    """
    在给定的二叉树中找到第二小的元素值。假设树中至少有两个不同的元素值，否则返回 -1。树中每个节点的值是其所有子节点的最小值。

    参数:
        root (TreeNode, 可选): 二叉树的根节点。

    返回:
        int: 树中第二小的元素值。如果所有节点值相同，返回 -1。
    """
    ans, rootvalue = -1, root.val
    def dfs(node: TreeNode) -> None:
        nonlocal ans
        if not node:
            return
        if ans != -1 and node.val >= ans:
            return
        if node.val > rootvalue:
            ans = node.val
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ans


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
    return self.searchBST(root.left if val < root.val else root.right, val)
