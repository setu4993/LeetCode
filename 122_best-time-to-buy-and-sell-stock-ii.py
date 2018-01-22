class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if prices:
            prev = prices[0]
            for pr in prices:
                if pr > prev:
                    profit += pr - prev
                    prev = pr
                else:
                    prev = pr
        return profit

print(Solution().maxProfit([7, 6, 5, 4, 6, 7]))