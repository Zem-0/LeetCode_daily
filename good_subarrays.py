from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        cnt = 0
        pair = 0
        n = len(nums)
        d = {}
        while r < n:
            pair += d.get(nums[r], 0)
            d[nums[r]] = d.get(nums[r], 0) + 1
            while pair >= k:
                cnt += n - r
                d[nums[l]] -= 1
                pair -= d[nums[l]]
                l += 1
            r += 1
        return cnt
