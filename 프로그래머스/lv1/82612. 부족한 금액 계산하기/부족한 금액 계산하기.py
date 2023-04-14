def solution(price, money, count):
    answer = -1
    
    total = 0
    for i in range(count):
        total += (price*(i+1))
            
    answer = total - money
    if answer < 0:
        answer = 0

    return answer