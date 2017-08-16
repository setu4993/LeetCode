import sys
sys.maxint = 32

class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        negative = False
        if x < 0:
            x = 0 - x
            negative = True

        while x != 0:
            x, quotient = divmod(x, 10)
            try:
                rev = rev * 10 + quotient
            except OverflowError:
                return 0
            pass
        if negative:
            rev = 0 - rev
        if rev > 2147483647 or rev <-2147483648:
            rev = 0
        return int(rev)

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(2147483651))