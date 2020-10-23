#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # intuition: turtoise and hare algorithm
        # first define a function by which we obtain the sum of the digits
        # the goal is to walk both turtoise and hare until they both meet or until the hare becomes 1. 
        # logic: while the turtoise is not equal to hare or, while the hare is not 1: we have a while loop where the turtoise is walking one step at a time while the hare is taking two steps at a time.
        
        getSumOfDigits = lambda n: sum(int(digit)**2 for digit in str(n)) # obtain sum of digits to the 2nd power in a number
        turtoise = n # 19
        hare = getSumOfDigits(n)
        while turtoise != hare and hare != 1:
            # move turtoise by one step
            # move hare by two steps
            turtoise = getSumOfDigits(turtoise) # one step
            hare = getSumOfDigits(getSumOfDigits(hare)) # two steps
        return hare == 1

# @lc code=end

