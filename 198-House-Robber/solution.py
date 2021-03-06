class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        t0, t1 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            temp = t1
            t1 = max(t1, t0 + nums[i])
            t0 = temp
        return t1
            
            