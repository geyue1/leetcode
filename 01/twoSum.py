# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> twoSum.py
@Author : yge
@Date : 2023/2/2 13:35
@Desc :

==============================================================
'''
'''
https://leetcode.cn/problems/two-sum/
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

'''
from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        for i in nums:
            j = target-i
            # print(f"j={j}")
            # print(nums[nums.index(i):])
            # print(nums)
            i_index = nums.index(i)
            temp_nums = nums[i_index+1:]

            if temp_nums.count(j)>0:
                return [i_index,temp_nums.index(j)+i_index+1]
        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        l = len(nums)
        for i in range(l):
            j = target-nums[i]
            if j in d:
                return [d[j],i]
            d[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution2()
    print(s.twoSum([2,7,11,15,15,15],30))