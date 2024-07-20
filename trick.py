def neighbor(x: int, y: int) -> Tuple[[int, int]]:
    for dx, dy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
        if 0 <= dx < n and 0 <= dy < m:
            yield dx, dy

isLeafNode = lambda node : not node.left and not node.right
