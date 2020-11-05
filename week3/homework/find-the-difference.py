# https: // leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dictionary = {}
        for chr in s:
            dictionary[chr] = dictionary.get(chr, 0) + 1
        for chr in t:
            if dictionary.get(chr, 0) == 0:
                return chr
            else:
                dictionary[chr] -= 1
