def largest_triangle_area(points: List[List[int]]) -> float:
    """
    计算给定点集中所有可能三角形的最大面积。
    
    使用三点确定的矩阵行列式方法计算面积。
    
    Args:
        points (List[List[int]]): 点集，每个点是一个包含两个整数的列表 [x, y]。

    Returns:
        float: 所有可能的三角形中面积的最大值。
    """
    from itertools import combinations
    def triangle_area(p1: List[int], p2: List[int], p3: List[int]) -> float:
        import numpy as np
        matrix = np.array([p1 + [1], p2 + [1], p3 + [1]])
        return 0.5 * abs(np.linalg.det(matrix))
    
    return max(triangle_area(p1, p2, p3) for p1, p2, p3 in combinations(points, 3))