def list_sub(current, prev):
    years = current[0]-prev[0]
    months = current[1]-prev[1]
    if months < 0:
        years-=1
        months+=12
    days = current[2]-prev[2]
    if days < 0:
        months-=1
        days+=28
    
    if years > 0:
        months = months + years*12
    return months

def solution(today, terms, privacies):
    answer = []
    
    today = list(map(int, today.split('.')))
    
    terms = list(map(lambda x: x.split(), terms))
    terms = list(map(lambda x: (x[0], int(x[1])), terms))
    
    privacies = list(map(lambda x: x.split(), privacies))
    for i in range(len(privacies)):
        for term in terms:
            if privacies[i][1] == term[0]:
                start = list(map(int, privacies[i][0].split('.')))
                diff = list_sub(today, start)
                if diff >= term[1]:
                    answer.append(i+1)
    return answer