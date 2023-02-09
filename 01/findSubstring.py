
# -* UTF-8 *-
'''
==============================================================
@Project -> File : leetcode -> findSubstring.py
@Author : yge
@Date : 2023/2/7 15:36
@Desc :

==============================================================
'''
'''
https://leetcode.cn/problems/substring-with-concatenation-of-all-words/
'''
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = []
        n = len(words)
        # 边界条件
        if len(s)<n*len(words[0]):
            return l
        temp = [] # 初始化滑动窗口
        step = len(words[0])
        for i in range(len(s)):
            temp.append(s[i])
            while len(temp)>n*step: #保证滑动窗口长度
                del temp[0]
            if len(temp)==n*step:
                temp_str = "".join(temp)
                temp_ = []
                for j in range(0,len(temp_str),step):
                    temp_.append(temp_str[j:j+step])
                flag = True
                for b in words:
                    if not b in temp_:
                        flag = False
                        break
                    else:
                        temp_.remove(b)
                if flag:
                    l.append(i+1-n*step)

        return l

from collections import Counter
class Solution2:
    '''
     使用hash映射
    '''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = []
        n = len(words)
        #temp = []  # 初始化滑动窗口
        step = len(words[0])
        for i in range(len(s)):
            if len(s)-i<n*step:
                break
            counter = Counter()
            for j in range(0,n):
                word = s[i+j*step:i+(j+1)*step]
                counter[word]+=1
            for w in words:
                counter[w]-=1
                if counter[w]==0:
                    del counter[w]
            if len(counter)==0:
                l.append(i)
        return l

from collections import Counter
class Solution3:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        m, n, ls = len(words), len(words[0]), len(s)
        for i in range(n):
            if i + m * n > ls:
                break
            differ = Counter()
            for j in range(m):
                word = s[i + j * n: i + (j + 1) * n]
                differ[word] += 1
            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            for start in range(i, ls - m * n + 1, n):
                if start != i:
                    word = s[start + (m - 1) * n: start + m * n]
                    differ[word] += 1
                    if differ[word] == 0:
                        del differ[word]
                    word = s[start - n: start]
                    differ[word] -= 1
                    if differ[word] == 0:
                        del differ[word]
                if len(differ) == 0:
                    res.append(start)
        return res

if __name__=="__main__":
    print("-----------s1-----------")
    s = Solution()
    print(s.findSubstring("barfoothefoobarman",["foo","bar"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
    #
    print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))

    print(s.findSubstring("ababaab",["ab","ba","ba"]))
    print("-----------s2-----------")
    s2 = Solution2()
    print(s2.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(s2.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
    print(s2.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    #
    print(s2.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))

    print(s2.findSubstring("ababaab", ["ab", "ba", "ba"]))
    print("-----------s3-----------")
    s3 = Solution3()
    print(s3.findSubstring("barfoothefoobarman", ["foo", "bar"]))