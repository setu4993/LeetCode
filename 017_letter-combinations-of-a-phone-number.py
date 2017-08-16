class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_alpha = {'': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        if len(digits) > 1:
            combinations = []
            digits_1 = Solution().letterCombinations(digits[1:])
            for k in num_alpha[digits[0]]:
                for j in digits_1:
                    combinations.append(k + j)
            return combinations
        else:
            return num_alpha[digits]

print(len(Solution().letterCombinations("67")))