class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sols = []
        for i, c in enumerate(candidates):
            if target - c > 0:
                lower = Solution().combinationSum(candidates[i:], target - c)
                for l in lower:
                    l.insert(0, c)
                    sols.append(l)
                pass
            elif target - c == 0:
                sols.append([c])
            else:
                continue
        return sols


print(Solution().combinationSum([2, 3, 6, 7], 7))