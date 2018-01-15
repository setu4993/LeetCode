class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current = "1"
        for i in range(1, n):
            count = 1
            next = []
            j = 1
            while j < len(current):
                if current[j] == current[j - 1]:
                    count += 1
                    j += 1
                else:
                    next.append(str(count))
                    next.append(current[j - 1])
                    j += 1
                    count = 1
            next.append(str(count))
            next.append(current[j - 1])
            current = "".join(next)
        return current


print(Solution().countAndSay(5))