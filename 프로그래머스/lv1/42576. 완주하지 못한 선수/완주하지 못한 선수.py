from collections import Counter

def solution(participant, completion):
    answer = (Counter(participant)-Counter(completion)).most_common()[0][0]
    
    return answer