class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        a=(n+1)//2
        b=n//2
        res=1
        res = (pow(5, a, mod) * pow(4, b, mod)) % mod
        return res

        