class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s, dict_t = dict(), dict()
        for ch in list(s):
            if ch not in dict_s:
                dict_s[ch] = 1
            else:
                dict_s[ch] += 1
        for ch in list(t):
            if ch not in dict_t:
                dict_t[ch] = 1
            else:
                dict_t[ch] += 1

        if dict_s==dict_t:
            return True
        else:
            return False
