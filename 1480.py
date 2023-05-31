"""
https://leetcode.com/problems/running-sum-of-1d-array/description/
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # trail #1
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
        
        # trail #2
        # for i, j in zip(range(1, len(nums)), range(len(nums)-1)):
        #     nums[i] += nums[j]
        # return nums

        # trail #3
        # return [sum(nums[:i]) for i in range(1, len(nums)+1)]
