# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> reverse.py
@Author : yge
@Date : 2023/2/17 16:42
@Desc :
https://leetcode.cn/problems/reverse-integer/
==============================================================
'''
'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
----------------------
输入：x = 123
输出：321
----------------------
输入：x = -123
输出：-321
----------------------
输入：x = 0
输出：0
'''
import math
class Solution:
    def reverse(self, x: int) -> int:

        s = str(x)
        is_negative = False
        if s.startswith("-"):
            is_negative = True
            s = s[1:]
        s_ = s[::-1]
        value = 0
        if is_negative:
            value = int("-"+s_)
        else:
            value = int(s_)
        if value>math.pow(2,31)-1 or value<-math.pow(2,31):
            return 0
        else:
            return value

if __name__=="__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(0))
    print(s.reverse(1534236469))