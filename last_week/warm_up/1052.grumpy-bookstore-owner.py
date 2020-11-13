#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        i = currWindow = maxWindow = satisfied = 0
        for customer, g in zip(customers, grumpy):
            satisfied += customer * (1-g)
            currWindow += customer * g
            if i >= X:
                currWindow -= customers[i-X] * grumpy[i-X]
            maxWindow = max(maxWindow, currWindow)
            i += 1
        return satisfied + maxWindow

    def maxSatisfied2(self, customers, grumpy, X):
        n = len(customers)
        res = sum(customers[i] * (1 - grumpy[i]) for i in range(n)) # total gain from customers in non-grumpy minutes
        max_gain = sum(customers[i] * grumpy[i] for i in range(X)) # maximum gain from customers using the secret technique for X grumpy minutes
        gain = max_gain
        for i in range(X, n):
            gain += customers[i] * grumpy[i] - customers[i-X] * grumpy[i-X]
            max_gain = max(max_gain, gain) # add the new and kick the old only if during grumpy minutes, for we don't want to deal with duplicate customers
        return res + max_gain
# @lc code=end

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
ans = Solution().maxSatisfied(customers, grumpy, X)
print(ans)