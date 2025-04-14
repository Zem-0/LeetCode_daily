from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        res.append(0)
        if len(nums)==0:
            return 0
        def backtrack(i,curr):
            if i>=len(nums):
                res.append(curr)
                return res
            take=backtrack(i+1,curr^nums[i])
            notake=backtrack(i+1,curr)
        backtrack(0,0)
        return sum(res)

            

        