class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float('inf')
        max_price=  0
        for p in prices:
            mini = min(p,mini)
            max_price = max(max_price,p-mini)
        return max_price