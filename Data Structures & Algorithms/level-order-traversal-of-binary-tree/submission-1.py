# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        level = 0

        while q:
            res.append([])
            for i in range(len(q)):
                n = q.popleft()
                res[level].append(n.val)

                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            level += 1
        
        return res

        