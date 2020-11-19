class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        counter[0] = -1

        maxCount = 0
        count = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                count = count - 1

            if count in counter:
                maxCount = max(maxCount, i - counter[count])
            else:
                counter[count] = i

        return maxCount
