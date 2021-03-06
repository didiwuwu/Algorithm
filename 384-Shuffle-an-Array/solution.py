import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.origin = nums
        self.nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.origin[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.nums)
        for i in range(n - 1, -1, -1):
            index = random.randrange(0, i + 1, 1)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()