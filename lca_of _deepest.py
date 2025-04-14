from collections import defaultdict
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d=defaultdict(list)
        def dfs(node,depth):
            if not node:
                return
            d[depth].append((node.val))
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        maxu=max(d.keys())
        deep=d[maxu]
        if len(deep)==1:
            return deep[0]
        p,q=deep
        def lcs(root,p,q):
            if not root or root==p or root==q:
                return root
            left=lcs(root.left,p,q)
            right=lcs(root.right,p,q)
            if left and right:
                return root
            return left or right
        res=deep[0]
        for n in deep[1:]:
            res=lcs(root,res,n)
        return res
   

            

            
        