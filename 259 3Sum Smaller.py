"""
Premium Question
Smaller than the target.
Author: Rajeev Ranjan

"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """

        :type nums: list[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cnt = 0
        n = len(nums)
        for i in xrange(n-2):
            l = i+1
            h = n-1
            while l < h:
                if nums[i]+nums[l]+nums[h] < target:
                    cnt += h-l  # move the high ptr leftward till low.
                    l += 1
                else:
                    h -= 1

        return cnt
