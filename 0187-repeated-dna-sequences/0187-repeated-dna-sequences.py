class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = set()
        for i in range(len(s)-10):
            if s[i:i+10] in s[i+1:]:
                answer.add(s[i:i+10])
        answer = list(answer)
        return answer