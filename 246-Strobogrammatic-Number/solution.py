class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in dict or num[right] not in dict:
                return False
            if num[left] != dict[num[right]]:
                return False
            left += 1
            right -= 1
        return True
