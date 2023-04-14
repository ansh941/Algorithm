from collections import deque
import math

def solution(picks, minerals):
    # 가장 작은 경우를 추출하기 때문에 비교군은 최대로
    answer = math.inf
    
    # BFS를 통해 탐색할 예정
    q = deque()
    # 현재 피로도와 남은 곡괭이, 남은 광물로 초기값을 세팅
    q.append((0, picks, minerals))
    
    # 각 광물에 대한 리스트와 곡괭이 사용 피로도에 대한 딕셔너리 정의
    mineral_class = ['diamond', 'iron', 'stone']
    pick_dict = {'diamond':[1,1,1], 'iron':[5,1,1], 'stone':[25,5,1]}
    
    while q:
        cur_result, cur_picks, cur_minerals = q.popleft()
        
        # 현재 피로도가 이미 구한 피로도보다 크면 굳이 이후를 진행할 필요가 없음
        if cur_result > answer:
            continue
        
        # 남은 곡괭이나 광물이 없으면 중지하는데
        if sum(cur_picks) == 0 or len(cur_minerals) == 0:
            # 현재까지 측정된 피로도가 이전에 구한 피로도보다 작으면 저장
            if cur_result < answer:
                answer = cur_result
            continue
        
        # 각 곡괭이마다 계산
        for i in range(3):
            # 이번 피로도값 초기화
            plus_result = 0
            # 각 곡괭이가 남아있다면
            if cur_picks[i] > 0:
                new_picks = cur_picks.copy()
                # 해당 곡괭이 사용
                new_picks[i] -= 1
                
                # 가장 앞에 광물부터 최대 5개 채취
                for j in range(min(len(cur_minerals), 5)):
                    # 리스트에서 광물의 번호를 얻어 사용하는 곡괭이에 매겨진 피로도를 가져와 더한다.
                    idx = mineral_class.index(cur_minerals[j])
                    plus_result += pick_dict[mineral_class[i]][idx]
                # 이번 작업을 수행한 피로도와 사용한 곡괭이, 채취한 광물을 제외하고 큐에 추가
                q.append((cur_result+plus_result, new_picks, cur_minerals[5:]))
    
    return answer