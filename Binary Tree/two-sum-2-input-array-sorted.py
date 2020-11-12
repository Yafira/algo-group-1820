# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            left = 0
            right = len(numbers) - 1
            
            while left != right:
                sum = numbers[left] + numbers[right]
                
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    return [left + 1, right + 1] 

