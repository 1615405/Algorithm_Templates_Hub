class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        rank = defaultdict(int)
        stack = []

        for index, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                rank[stack.pop()] = price
            stack.append(index)
        
        while stack:
            rank[stack.pop()] = 0
        
        return [price - rank[index] for index, price in enumerate(prices)]
