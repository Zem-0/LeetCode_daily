class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1:
            return 0
        splits=[]
        for i in range(len(weights)-1):
            splits.append(weights[i]+weights[i+1])
        splits.sort()
        maxi=weights[0]+weights[-1]+sum(splits[-(k-1):])
        mini=weights[0]+weights[-1]+sum(splits[:k-1])
        return maxi-mini