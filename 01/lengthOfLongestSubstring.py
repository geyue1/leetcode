# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> lengthOfLongestSubstring.py
@Author : yge
@Date : 2023/2/7 10:11
@Desc :

==============================================================
'''
'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
          brute force algorithm

        '''
        n = len(s)
        if n==0:
            return 0
        count = []
        for i in range(n):
            j = i+1
            temp = [s[i]]
            while j<n:
                if not s[j] in temp:
                    temp.append(s[j])
                else:
                    break
                j+=1
            count.append(len(temp))
        return max(count)

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
          brute force algorithm
        :param s:
        :return:
        '''
        n = len(s)
        count = 0
        if n==0:
            return 0
        for i in range(n):
            j = i+1
            temp = [s[i]]
            while j<n:
                if not s[j] in temp:
                    temp.append(s[j])
                else:
                    break
                j+=1
            if len(temp)>count:
               count = len(temp)

        return count
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
          optimise algorithm
          滑动窗口
        :param s:
        :return:
        '''
        n = len(s)
        if n==0:
            return 0
        # if not s : return 0
        max_ = 0
        temp = []  #临时队列
        for a in s:
            while a in temp:
                del temp[0]
            temp.append(a)
            if len(temp)>max_:
                max_ = len(temp)
        return max_
if __name__=="__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkewa"))

    s2 = Solution2()
    print(s2.lengthOfLongestSubstring("abcabcbb"))
    print(s2.lengthOfLongestSubstring("bbbbb"))
    print(s2.lengthOfLongestSubstring("pwwkewa"))

    s3 = Solution3()
    print(s3.lengthOfLongestSubstring("abcabcbb"))
    print(s3.lengthOfLongestSubstring("bbbbb"))
    print(s3.lengthOfLongestSubstring("pwwkewa"))