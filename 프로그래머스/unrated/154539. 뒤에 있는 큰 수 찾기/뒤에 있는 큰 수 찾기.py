from collections import deque

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    
    q = deque()
    q.append((0, numbers[0]))
    
    idx = 1
    while idx < len(numbers):
        comp_num = numbers[idx]
        while q:
            num_idx, num = q.popleft()
            if comp_num > num:
                answer[num_idx] = comp_num
            else:
                q.appendleft((num_idx, num))
                break
        q.appendleft((idx, comp_num))
        idx+=1
    
    return answer