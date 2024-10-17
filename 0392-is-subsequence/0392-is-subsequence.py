class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_idx = -1

        for s_char in s:
            if s_char in t[t_idx+1:] and t_idx+1 <= len(t)-1:
                t_idx += t[t_idx+1:].index(s_char) + 1
            else:
                return False
        return True