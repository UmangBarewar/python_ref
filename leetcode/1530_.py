class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return []

            # If it's a leaf node, return a list with a single element (distance 1)
            if not node.left and not node.right:
                return [1]

            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            # Check all pairs between left and right distances
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        self.count += 1

            # Return the list of all distances incremented by 1
            return [d + 1 for d in left_distances + right_distances]

        dfs(root)
        return self.count
