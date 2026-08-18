import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_log = collections.defaultdict(int)
        t_log = collections.defaultdict(int)

        for char in s:
            s_log[char]+=1

        for char in t:
            t_log[char]+=1

        return s_log == t_log
