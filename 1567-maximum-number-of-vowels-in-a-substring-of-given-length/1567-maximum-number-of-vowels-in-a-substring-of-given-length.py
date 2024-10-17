class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        answer = 0
        for i in range(len(s)-k+1):
            count = 0
            for vowel in vowels:
                count += s[i:i+k].count(vowel)
            answer = max(answer, count)
        return answer