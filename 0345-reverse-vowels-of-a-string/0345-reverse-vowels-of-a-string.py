class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']

        lower_str = s.lower()

        answer = []
        vowel_indices = []
        for i in range(len(s)):
            if lower_str[i] in vowels:
                vowel_indices.append(i)
            else:
                answer.append(s[i])
        
        for vowel_index_forward, vowel_index_revserse in zip(vowel_indices, vowel_indices[::-1]):
            answer.insert(vowel_index_forward, s[vowel_index_revserse])
        return ''.join(answer)