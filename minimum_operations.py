from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        cnt=0
        arr=list(set(nums))
        for  n in arr:
            if n >k :
                cnt+=1
        return cnt

        