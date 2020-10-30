# https://leetcode.com/problems/find-common-characters

import collections
from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        compare = collections.Counter(A[0])
        
        for i in A:
            compare &= collections.Counter(i)
            
        return list(compare.elements())