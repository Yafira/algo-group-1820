#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        '''
        use dfs to find each child's parent and its depth. create a dictioanry to map each child's to its parent and depth. 
        at the end check if they're cousins: same depth, different parents

        dictionary:
            - [key: child node]: (parent node, depth)
        '''
        def dfs(node, depth): # o(n); o(h)
            for child in (node.left, node.right):
                if child:
                    if child.val in (x, y):
                        dic[child.val] = node.val, depth
                        # map child to a tuple of (parent node, depth)
                    dfs(child, depth+1)
        dic = {}
        dfs(root, 0)
        X, Y = dic.get(x, (-1, -1)), dic.get(y, (-2, -2)) # 0 and 1 are default values to make them not cousins
        print(X, Y)
        return X[0] != Y[0] and X[1] == Y[1]
# @lc code=end

