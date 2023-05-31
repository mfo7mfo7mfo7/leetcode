"""
https://leetcode.com/problems/unique-number-of-occurrences/description/
"""

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = Counter(arr)
        return True if len(set(a.values())) == len(a) else False
