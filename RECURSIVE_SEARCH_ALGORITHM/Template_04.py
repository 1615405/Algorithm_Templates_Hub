def minimumOperations(nums: List[int], start: int, goal: int) -> int:
      """
      使用双向广度优先搜索（Bidirectional BFS）计算将整数 start 转换为整数 goal 所需的最小操作数。
      操作包括对当前整数进行加、减或异或（XOR）处理，每次操作使用 nums 数组中的任一数字。
      """
      q1, q2 = deque([start]), deque([goal])
      vis1, vis2 = {start: 0}, {goal: 0}

      def update(que, vis_this, vis_other) -> int:
          while que:
              current = que.popleft()
              step = vis_this[current]

              for num in nums:
                  for next_val in ((current + num), (current - num), (current ^ num)):
                      if next_val in vis_other:
                          return step + 1 + vis_other[next_val]
                      if 0 <= next_val <= 1000 and next_val not in vis_this:
                          vis_this[next_val] = step + 1
                          que.append(next_val)

          return -1
      
      while q1 and q2:
          if len(q1) < len(q2):
              ans = update(q1, vis1, vis2)
              if ans != -1:  return ans
          else:
              ans = update(q2, vis2, vis1)
              if ans != -1:  return ans
      
      return -1
