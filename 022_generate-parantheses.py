class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parantheses = []
        def paranthesis(open, close, parenstring = ""):
            if close >= open:
                if open:
                    paranthesis(open - 1, close, parenstring + "(")
                if close:
                    paranthesis(open, close - 1, parenstring + ")")
                if open == close and open == 0:
                    print(parenstring)
                    parantheses.append(parenstring)
        paranthesis(n - 1, n, "(")

        return parantheses
        '''        
        if n > 1:
            generated = Solution().generateParenthesis(n - 1)
            for g in generated:
                parantheses.append("(" + g + ")")
                parantheses.append("()" + g)
                if g + "()" != "()" + g:
                    parantheses.append(g + "()")
            return parantheses
        elif n == 1:
            return ["()"]
        else:
            return []
        '''
# print(Solution().generateParenthesis(2))
# print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))

# ['()(())()']

# ["(())(())"]