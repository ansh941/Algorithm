l = []
c = ['A', 'E', 'I', 'O', 'U']

def all_words(w, length):
    global l, c
    if length >= 5:
        return
    for i in range(len(c)):
        l.append(w+c[i])
        all_words(w+c[i], length+1)
    
def solution(word):
    answer = 0
    
    all_words('', 0)
    answer = l.index(word)+1
    
    return answer