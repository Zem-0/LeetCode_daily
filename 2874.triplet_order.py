from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_left=[0]*len(nums)
        max_left[0]=nums[0]
        res=0
        n=len(nums)
        for i in range(1,len(nums)):
            max_left[i]=(max(nums[i],max_left[i-1]))
        max_right=[-1]*len(nums)
        max_right[-1]=nums[-1]
        for j in range(n-2,-1,-1):
            max_right[j]=max(max_right[j+1],nums[j])
        for i in range(1,len(nums)-1):
            if max_left[i-1]>nums[i] and max_right[i+1]>0:
                r=(max_left[i-1]-nums[i])*max_right[i+1]
                res=max(r,res)
        return res