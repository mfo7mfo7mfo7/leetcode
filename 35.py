"""
https://leetcode.com/problems/search-insert-position/description/
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif  target > nums[-1]:
            return len(nums)
        
        total_ = len(nums)
        i = int(total_/2)
        run=1
        while True:
            if nums[i] < target:
             
                if target <= nums[i+1]:
                    break
                else:
                    i += math.ceil((total_ - i+1)/(2**run))
            else:

                i -= math.ceil((i)/(2**run))
            run += 1
        return i + 1
    
