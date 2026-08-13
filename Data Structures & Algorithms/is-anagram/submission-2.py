class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_cnt_s = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
        dict_cnt_t = {chr(i):0 for i in range(ord('a'), ord('z') + 1)}
        for si, ti in zip(s,t):
            dict_cnt_s[si] += 1
            dict_cnt_t[ti] += 1
        return True if dict_cnt_s == dict_cnt_t else False

        