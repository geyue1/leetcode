# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> countSubstrings.py
@Author : yge
@Date : 2023/2/13 13:45
@Desc :
https://leetcode.cn/problems/palindromic-substrings/
==============================================================
'''
'''
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
----------------------------------
输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
-----------------------------------
输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
----------------------------------
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        s_ = "#"+"#".join(s)+"#"
        n = len(s_)
        for i in range(n):
            k1 = i-1
            k2 = i+1
            l = 0
            while k1>=0 and k2<n:
                if s_[k1:i] == s_[i+1:k2+1][::-1]:
                    sub_str = s_[k1:k2+1]
                    l_ = len(sub_str.replace("#",""))
                    if not l_==l:
                         count+=1
                l = l_
                k1-=1
                k2+=1
        return count
class Solution2:
    def countSubstrings(self, s: str) -> int:
        '''
         dynamic programming algorithm
        :param s:
        :return:
        '''
        #定义并初始化数组
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        count = 0
        #循环遍历
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = True
                    count +=1
                elif j-i == 1 and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
                elif dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j] = True
                    count += 1
        return count






if __name__=="__main__":

    s = Solution()
    print(s.countSubstrings("abx"))
    print(s.countSubstrings("aaa"))

    s2 = Solution2()
    print(s2.countSubstrings("abx"))
    print(s2.countSubstrings("aaa"))


