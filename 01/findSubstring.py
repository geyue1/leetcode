
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
        if len(s)<n*len(words[0]):
            return l
        temp = []
        step = len(words[0])
        for i in range(len(s)):
            temp.append(s[i])
            while len(temp)>n*step:
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

if __name__=="__main__":
    s = Solution()
    print(s.findSubstring("barfoothefoobarman",["foo","bar"]))
    print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
    print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
    #
    print(s.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))

    print(s.findSubstring("ababaab",["ab","ba","ba"]))