T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def hex2ten(num_list):
    for i in range(len(num_list)):
        num_list[i] = int('0x'+num_list[i], 16)
    return num_list

def rotation(str):
    tmp = str[-1]
    str = tmp+str[:-1]
    return str

def split_num(str, length):
    str_set = {str[i*length:i*length+length] for i in range(4)}
    return str_set


#for test_case in range(1, 2):
for test_case in range(1, T + 1):
    num_set = set()
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    str = input()
    
    # 16진수 숫자 길이
    num_len = N//4
    
    for i in range(num_len):
        num_set.update(split_num(str, num_len))
        str = rotation(str)
    num_list = list(num_set)
    num_list = hex2ten(num_list)
    num_list.sort()
    num_list.reverse()
    print('#{} {}'.format(test_case, num_list[K-1]))
    
    # ///////////////////////////////////////////////////////////////////////////////////
