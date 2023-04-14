L, C = map(int, input().split())
chars = list(input().split())

from copy import deepcopy

def check(string):
    mo = 0
    ja = 0
    moum = ['a', 'e', 'i', 'o', 'u']
    
    for i in string:
        for j in range(5):
            if i == moum[j]:
                mo += 1
    ja = len(string) - mo
    if mo > 0 and ja > 1:
        return True
    else:
        return False

chars.sort()

def make_password(n, alpha, password):
    if len(password) == n:
        if check(password):
            print(password)
        return
    if len(alpha) < n-len(password):
        return
    
    for i in range(len(alpha)):
        next_alpha= deepcopy(alpha)
        add_char = next_alpha[i]
        idx = next_alpha.index(add_char)
        next_alpha = next_alpha[idx+1:]
        make_password(n, next_alpha, password+add_char)

for i in range(C-L+1):
    make_password(L, chars[i+1:], chars[i])
