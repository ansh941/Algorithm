def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()
    
    recon_id = ''
    for char in new_id:
        if char.isalpha() or char.isdigit() or char == '-' or char == '_' or char == '.':
            recon_id += char
    new_id = recon_id
            
    recon_id = ''
    temp = ''
    for i in range(len(new_id)):
        if new_id[i] == '.':
            temp += '.'
        else:
            if len(temp) >= 1:
                recon_id += '.'
                temp = ''
            recon_id += new_id[i]
    new_id = recon_id

    new_id = new_id.strip('.')
    
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    if len(new_id) <= 2:
        length = len(new_id)
        char = new_id[-1]
        for i in range(3-length):
            new_id+=char
    answer = new_id
    return answer