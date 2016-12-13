'''
This is my initial solution. Probably not optimal, but it's likely close.
'''
class LeetcodeSolution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right: return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
