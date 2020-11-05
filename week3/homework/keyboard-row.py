# https: // leetcode.com/problems/keyboard-row/

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = {}
        for c in "qwertyuiopQWERTYUIOP":
            row[c] = 1
        for c in "asdfghjklASDFGHJKL":
            row[c] = 2
        for c in "zxcvbnmZXCVBNM":
            row[c] = 3

        result = []
        for word in words:
            if len(set(row[c] for c in word)) == 1:
                result.append(word)
        return result
