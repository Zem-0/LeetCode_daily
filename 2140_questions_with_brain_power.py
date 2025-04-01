class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp={}
        def dfs(i,curr):
            if i>=len(questions):
                return 0
            if (i,curr) in dp:
                return dp[(i,curr)]
            a=questions[i][0]+dfs(i+questions[i][1]+1,curr)
            b=dfs(i+1,curr)
            dp[(i,curr)]=max(a,b)
            return dp[(i,curr)]
        return dfs(0,0)
