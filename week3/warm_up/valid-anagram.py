#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
from collections import defaultdict
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        counter = defaultdict(int) 
        for char in s:
            counter[char] += 1
        for char in t:
            counter[char] -= 1
            if counter[char] < 0: # for each character i'm looping, i want to see if its frequency ever goes below 0. if it does, then we have a mismatch
                return False
        return True
# @lc code=end

s = 'look'
t = 'book'
ans = Solution().isAnagram(s, t)
print(ans)