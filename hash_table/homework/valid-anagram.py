# https://leetcode.com/problems/valid-anagram

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return "".join(sorted(s)) == "".join(sorted(t))

    s = "listen"
    t = "silent"
    isAnagram(bool, s, t)

    if(sorted(s) == sorted(t)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")