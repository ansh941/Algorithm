from collections import deque
import math

def comp(max_val, cur_val):
    return sorted([max_val, cur_val], reverse=True)[0]
    
def buy(users, emoticons, emo_sale_ratios):
    value = [0,0]
    for user in users:
        inter_value = [0,0]
        for i, emoticon in enumerate(emoticons):
            if user[0] >= emo_sale_ratios[i]:
                inter_value[1] += emoticon*emo_sale_ratios[i]
        if user[1] <= round(inter_value[1],1):
            value[0] += 1
        else:
            value[1] += round(inter_value[1],1)
    return value

def solution(users, emoticons):
    answer = []
    
    min_ratio = 40
    
    # 유저들 중 가장 적은 할인율 찾기
    # 20% 할인 -> 0.8의 형식으로 바꾸기
    for idx, user in enumerate(users):
        if min_ratio > user[0]:
            min_ratio = user[0]
        users[idx][0] = 1 - (users[idx][0]/100)
        
    
    # 가장 적은 할인율도 위 형식으로 변환
    inverse_ratio = 1-(min_ratio/100)
    inverse_ratio /= 0.1
    inverse_ratio = round(inverse_ratio, 1)
    inverse_ratio = min(round(inverse_ratio*0.1, 1), 0.9)
    
    # 이를 초기값으로 활용
    init_val = inverse_ratio
    
    # 할인율 정의 및 필요없는 것 제거
    sale_ratio = [0.9, 0.8, 0.7, 0.6]
    sale_idx = sale_ratio.index(init_val)
    sale_ratio = sale_ratio[sale_idx:]
    
    # 초기 할인율 enqueue
    q = deque()
    q.append(([init_val]*len(emoticons), 0))
    
    # 초기 할인율에 따라 maximum value 초기화
    max_value = [0,0]
    max_value = buy(users, emoticons, [init_val]*len(emoticons))

    # 탐색
    visited = []
    while q:
        # 현재 할인율 및 할인율을 바꿔줄 이모티콘의 index
        emo_sale_ratios, idx = q.popleft()
        
        # 현재 할인율에 따른 value 계산
        cur_value = buy(users, emoticons, emo_sale_ratios)
        # maximum value 와 비교
        max_value = comp(max_value, cur_value)
        
        # 아이템 수보다 많으면 pass
        if idx >= len(emo_sale_ratios):
            continue
        
        for i in range(0, len(sale_ratio)):
            # 할인율 적용
            new_ratios = emo_sale_ratios.copy()
            new_ratios[idx] = sale_ratio[i]
            
            # 이 세팅을 이미 이전에 봤다면 continue
            if new_ratios in visited:
                continue
            # 아니면 enqueue
            visited.append(new_ratios)
            q.append((new_ratios, idx+1))
            
                
    answer = max_value
    return answer