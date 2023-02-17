# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> findMedianSortedArrays.py
@Author : yge
@Date : 2023/2/17 12:38
@Desc :
https://leetcode.cn/problems/median-of-two-sorted-arrays/
==============================================================
'''
'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。
-------------------
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
-------------------
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
-------------------
'''
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        n = len(nums)
        if n%2 == 0:
            return (nums[n//2-1]+nums[n//2])/2
        else:
            return nums[(n+1)//2-1]

if __name__=="__main__":

    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2]))
    print(s.findMedianSortedArrays([1, 2], [3,4]))
