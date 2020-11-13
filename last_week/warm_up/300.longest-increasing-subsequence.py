#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums):
        '''
        approach: have an array named tails storing the smallest tails of all increasing subsequences of length i + 1 in tails[i]
        for each num in the given list, if a num is greater than all tails, create a copy of the previous sequence and append the num; else, we can lower the bar and give it more room to increase sequence
        question: how do we know which tail to be updated?
        since the tails are by default sorted in ascending order, we can use binary search. 
        size - to store the max length of the increasing subseuqnce; only if the sequence has been extended.

        For this list, we can have LIS with different length.
        For length = 1, [1], [3], [5], [2], [8], [4], [6], we pick the one with smallest tail element as the representation of length=1, which is [1]
        For length = 2, [1,2] [1,3] [3,5] [2,8], ...., we pick [1,2] as the representation of length=2.
        Similarly, we can derive the sequence for length=3 and length=4
        The result sequence would be:
        len=1: [1]
        len=2: [1,2]
        len=3: [1,3,4]
        len=4: [1,3,5,6]

        According to the logic in the post,we can conclude that:
        (1) If there comes another element, 9
        We iterate all the sequences, found 9 is even greater than the tail of len=4 sequence, we then copy len=4 sequence to be a new sequece, and append 9 to the new sequence, which is len=5: [1,3,5,6,9]
        The result is:
        len=1: [1]
        len=2: [1,2]
        len=3: [1,3,4]
        len=4: [1,3,5,6]
        len=5: [1,3,5,6,9]

        (2) If there comes another 3,
        We found len=3 [1,3,4], whose tailer is just greater than 3, we update the len=3 sequence tobe [1,3,3]. The result is:
        len=1: [1]
        len=2: [1,2]
        len=3: [1,3,3]
        len=4: [1,3,5,6]

        (3) If there comes another 0,
        0 is smaller than the tail in len=1 sequence, so we update the len=1 sequence. The result is:
        len=1: [0]
        len=2: [1,2]
        len=3: [1,3,3]
        len=4: [1,3,5,6]
        '''
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            lo, hi = 0, size
            while lo < hi:
                mid = (lo + hi) // 2
                if tails[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            tails[lo] = x
            size = max(size, lo + 1)
        return size
# @lc code=end

nums = [1,3,5,2,8,4,6,9]
ans = Solution().lengthOfLIS(nums)
print(ans)