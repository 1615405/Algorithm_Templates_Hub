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
    def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
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
