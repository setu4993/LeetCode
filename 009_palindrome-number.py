class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 and x < 2147483647:
            num_range = 1
            while x > num_range:
                num_range *= 10
            while x >= 10 or num_range > 10:
                l, x = divmod(x, num_range / 10)
                x, r = divmod(x, 10)
                print(num_range, r, l, x)
                if l != r:
                    return False
                num_range /= 100
            return True

        return False

print(Solution().isPalindrome(1000021))