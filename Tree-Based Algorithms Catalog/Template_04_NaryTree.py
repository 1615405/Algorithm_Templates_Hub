# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


def preorder(root: 'Node') -> List[int]:
    """
    对一个 N 叉树进行前序遍历，返回遍历的节点值列表。
    
    参数:
        root (Node, 可选): N 叉树的根节点。
    
    返回:
        List[int]: 前序遍历的节点值列表。
    """
    ans = []
    def dfs(node: 'Node'):
        if not root:  return
        ans.append(node.val)
        for child in node.children:
            dfs(child)
    dfs(root)
    return ans


def postorder(root: 'Node') -> List[int]:
    """
    对一个 N 叉树进行后序遍历，返回遍历的节点值列表。
    
    参数:
        root (Node, 可选): N 叉树的根节点。
    
    返回:
        List[int]: 后序遍历的节点值列表。
    """
    ans = []
    def dfs(node: 'Node'):
        if node is None:  return
        for child in node.children:
            dfs(child)
        ans.append(node.val)
    dfs(root)
    return ans


def maxDepth(root: 'Node') -> int:
    """
    计算 N 叉树的最大深度。
    
    参数:
        root (Node, 可选): N 叉树的根节点。

    返回:
        int: 树的最大深度。
    """
    if not root:  return 0
    ans = 0
    for child in root.children:
        ans = max(ans, maxDepth(child))
    return ans + 1