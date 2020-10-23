#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s, t):
        # table1 matches the s[i] to t[i]
        # table2 matches the t[i] to s[i]
        # idea is to match letter from one string to letters from the other stirng. so that the next time we encounter the same letter, we check for its corresponding letter in s or t. if there's no match, return false immediately.
        table1, table2 = {}, {}
        for i in range(len(s)):
            if s[i] in table1 and table1[s[i]] != t[i]:
                return False
            if t[i] in table2 and table2[t[i]] != s[i]:
                return False
            # if the s[i] or t[i] does not yet exist in either tables, then store it accordingly.
            table1[s[i]] = t[i]
            table2[t[i]] = s[i]
        return True
        
    def isIsomorphic2(self, s, t):
        '''
        intuition: to use hash tables to store the first index of each new character in both strings
        logic: 
            - base: if the length is not same, return false right away (in an interview)
            - initialize two hash tables.
            goal #1. to record the first indexes of each new character as we traverse the strings. 
            goal #2 - traverse the strings once again, if the indices from the hash tables don't match, return fasle
        approach: 
            - two for loops.
            - first loop: goal #1
            - second loop: goal #2
        '''
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(s)): # for loop #1
            # mapping the character (as a key) to its relative index in the string
            dic1[s[i]] = dic1.setdefault(s[i], i)
            dic2[t[i]] = dic2.setdefault(t[i], i)

        # {'f': 0, 'o': 1} {'b': 0, 'a': 1, 'r': 2}
        for i in range(len(s)): # 2nd for loop to check for inconsistencies between the recorded first indexes.
            if dic1[s[i]] != dic2[t[i]]:
                return False
        return True
# @lc code=end

s, t = 'foo', 'bar'
s, t = 'paper', 'title'
s, t = 'egg', 'add'
ans = Solution().isIsomorphic(s, t)
print(ans)
