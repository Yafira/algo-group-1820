#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, A):
        '''
        (ex. nums[0] < nums[1] > nums[2] < nums[3] > ... ).
        turbulent subarray: when the comparison signs alternate between consecutive elements.

        3 scenarios: 
        1. if i >= 2:
            - check if the consecutive elements are turbulent.
            - increment currWindow by 1.
        2. if i >= 1 and nums[i] != nums[i-1]:
            - currWindow = 2
        3. else: currWindow = 1
        
        at the end of the iteration, update the maxWindow.
        '''
        currWindow = maxWindow = 0
        for i in range(len(A)):
            if i >= 2 and (A[i-2] < A[i-1] > A[i] or A[i-2] > A[i-1] < A[i]): # 3 consecutive elements
                currWindow += 1
            elif i >= 1 and A[i] != A[i-1]: # if the neighbor isn't equal. # 2 consecutive elements
                currWindow = 2
            else: # only one element.
                currWindow = 1
            # update maxWindow
            maxWindow = max(maxWindow, currWindow)
        return maxWindow
# @lc code=end
A = [9,4,2,10,7,8,8,1,9]
# edge cases
A = [9,9]
A = [4,8,12,16]
A = [100] 
A = [37,199,60,296,257,248,115,31,273,176]
ans = Solution().maxTurbulenceSize(A)
print(ans)
