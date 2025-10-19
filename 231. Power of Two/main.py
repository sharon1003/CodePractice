class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Method 1
        if (n & (n-1) == 0):
            return True
        else:
            return False

        # Method 2
        if n <= 0:
            return False

        count = 0
        while n:
            count += (n & 1)
            n = n >> 1

        if count > 1:
            return False
        else:
            return True