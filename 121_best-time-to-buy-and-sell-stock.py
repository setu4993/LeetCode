class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if prices:
            min = prices[0]
            for pr in prices:
                profit = max(profit, pr - min)
                if min > pr:
                    min = pr
        return profit

print(Solution().maxProfit([7, 0, 5, 3, 6, 7]))