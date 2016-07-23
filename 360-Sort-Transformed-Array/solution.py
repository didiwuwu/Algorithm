class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def func(num, a, b, c):
            return a * num * num + b * num + c
        
        if not nums:
            return []
        n = len(nums)
        result = []
        i, j = 0, n - 1
        if a >= 0:
            while i <= j:
                cand1, cand2 = func(nums[i], a, b, c), func(nums[j], a, b, c)
                if cand1 > cand2:
                    result.append(cand1)
                    i += 1
                else:
                    result.append(cand2)
                    j -= 1
            result = result[::-1]
        else:
            while i <= j:
                cand1, cand2 = func(nums[i], a, b, c), func(nums[j], a, b, c)
                if cand1 < cand2:
                    result.append(cand1)
                    i += 1
                else:
                    result.append(cand2)
                    j -= 1
        return result