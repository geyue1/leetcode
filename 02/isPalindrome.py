# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> isPalindrome.py
@Author : yge
@Date : 2023/2/17 10:32
@Desc :
https://leetcode.cn/problems/palindrome-number/
==============================================================
'''
'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
----------------------
输入：x = 121
输出：true
---------------------
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
---------------------
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
--------------------
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
       s = str(x)
       # return s == s[::-1]
       if s == s[::-1]:
           return True
       return False

if __name__=="__main__":

    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(2))