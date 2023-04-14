from collections import deque

def solution(storey):
    answer = 0
    
    new_storey = deque()
    for i in range(len(str(storey))):
        new_storey.append(int(str(storey)[i]))
    
    while new_storey:
        # 현재 층
        value = new_storey.pop()
        # 사용할 돌
        # 위랑 아래 중 어디가 이득인가 판단
        stone = min(10-value, value)
        answer += stone
        
        # 5보다 크면 위로 가는게 이득
        if value != stone:
            # 다음 자릿수가 있으면
            if new_storey:
                # 거기에 +1
                next_val = new_storey.pop()
                new_storey.append(next_val+1)
            # 없으면 자릿수 추가
            else:
                new_storey.appendleft(1)
        # 근데 딱 5인 경우 위 아래의 값이 같다
        elif value == 5:
            # 다음 자릿수를 보고 판단할 수 있는데
            # 65 -> 60 -> 100 -> 0
            # 65 -> 70 -> 100 -> 0
            if new_storey:
                next_val = new_storey.pop()
                # 다음 것도 5보다 크면 위로 가서 그 수에 자릿수를 보태주는게 이득
                if next_val >= 5:
                    new_storey.append(next_val+1)
                # 아니면 그냥 내려가는게 맞음
                else:
                    new_storey.append(next_val)
    return answer