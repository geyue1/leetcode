# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> fabnacii.py
@Author : yge
@Date : 2023/2/16 14:32
@Desc :

==============================================================
'''
import time
class Solution:
    def fabnacii(self,n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.fabnacii(n-1)+self.fabnacii(n-2)

class Solution2:
    def fabnacii(self,n):
        dp = [0]*(n+1)
        if n == 0:
            dp[0] = 1
        if n == 1:
            dp[0] = 1
            dp[1] = 1
        if n>=2:
            dp[0] = 1
            dp[1] = 1
            for i in range(2,n+1):
                dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

if __name__=="__main__":

    s1 = Solution()
    start = time.time()*1000
    print(s1.fabnacii(35))
    end = time.time()*1000
    print(f"{end-start} ms")

    s2 = Solution2()
    start2 = time.time()*1000

    print(s2.fabnacii(35))
    end2 = time.time()*1000
    print(f"{end2-start2} ms")
