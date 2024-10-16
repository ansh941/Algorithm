class Solution:
    def reverseWords(self, s: str) -> str:
        splits = s.split()

        return ' '.join(splits[::-1])