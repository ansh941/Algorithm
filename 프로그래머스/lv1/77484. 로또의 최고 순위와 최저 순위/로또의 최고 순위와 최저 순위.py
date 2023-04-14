def solution(lottos, win_nums):
    answer = []
    
    zeros = lottos.count(0)
    
    lottos = set(lottos)
    win_nums = set(win_nums)
    
    nums = 6-len(win_nums - lottos)
    
    h_score = min(7-(nums+zeros), 6)
    l_score = min(7-nums, 6)
    answer = [h_score, l_score]
    return answer