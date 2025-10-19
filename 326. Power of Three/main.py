class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Method 1
        if n < 0:
            return False
        
        while n % 3 == 0:
            n = n // 3

        if n == 1:
            return True
        else:
            return False


        # Method 2
        if n <= 0:
            return False
        if n == 1:
            return True

        while n:
            if n == 1 and n % 3 == 1:
                return True
            if n % 3 == 0:
                n = n / 3
            else:
                return False

        return True