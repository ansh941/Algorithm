N, M = map(int, input().split())
nums = [i+1 for i in range(N)]

def print_seq(seq):
    for i in range(M):
        print(seq[i], end=' ')
    print()
    
# 현재 수열, 선택 가능 숫자
def sequence(seq, n):
    if len(seq)==M:
        print_seq(seq)
        return
    
    for i in range(len(n)):
        next_seq = seq.copy()
        next_seq.append(n[i])
        next_n = n.copy()
        next_n.remove(n[i])
        sequence(next_seq, next_n)
        
sequence([],nums)