class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def find(a,b):
            c=sum([int(n) for n in a])
            d=sum([int(n) for n in b])
            return c==d
        cnt=0
        for n in range(low,high+1):
            a=str(n)
            if len(a)%2==0:
                l=len(a)
                b=a[:l//2]
                c=a[l//2:]
                if find(b,c):
                    cnt+=1
        return cnt
        