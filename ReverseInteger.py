class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(abs(x))
        s = s.strip()
        s = s[::-1]
        output = int(s)
        if output >= 2**31-1 or output <= -2**31-1:
            return 0
        elif x < 0:
            return -1*output
        else:
            return output