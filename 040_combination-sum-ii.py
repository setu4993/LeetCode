class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        sols = []
        seen = []
        for i, c in enumerate(candidates):
            if c not in seen:
                if target - c > 0:
                    lower = Solution().combinationSum2(candidates[i + 1:], target - c)
                    for l in lower:
                        l.insert(0, c)
                        # if l not in sols:
                        sols.append(l)
                    seen.append(c)
                elif target - c == 0:
                    # if [c] not in sols:
                    sols.append([c])
                    seen.append(c)
                else:
                    break
        return sols


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))