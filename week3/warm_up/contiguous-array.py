#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findMaxLength(self, nums):
        #intuition: a contiguous array is defined as having an equal number of 0s and 1s. how to store the frequency count of 0s and 1s at the same time?
        # action: declare a count value for whenever we see a zero, decrement count by 1. similarly, whenever we see a 1, increment count by 1. next, create a dictionary to mapping the count value to its very first corresponding index. it's fair to say that the next time we encounter the same count value, we have found a contiguous subarray; so then we will update the max_length by subtracting the current index by the old index. 
        #tricky: {0: -1}. why? nums = [0, 1] or [1, 0]. dic = {1: 0, 0: 1}; dic = {-1: 0, 0: 1}. we need soemthing initialized to be subtracted from the new index. as we scan the array from index 0 to n-1, it's best to initialize the dictionary with {0: -1}
        dic = {0: -1}
        count = max_length = 0
        for i, num in enumerate(nums):
            count += num or -1 # count is a variable tracking the frequency count of 0s and 1s. When we see a 0, decrement count by 1; else, increment count by 1. 
            if count not in dic:
                dic[count] = i # map the count value to its very first corresponding index upon which the subarray will eventually climb back up or down to the next time we see the same count value
            else: # time to update max_length
                max_length = max(max_length, i-dic[count])
        return max_length
# @lc code=end

S = Solution()
nums = [0, 1]
nums = [0,0,0,0,1,1,1]
nums = [0, 1, 0]
ans = S.findMaxLength(nums)
print(ans)