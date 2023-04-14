from collections import deque

# N : 수의 개수
# A : 각 숫자
N = int(input())
A = list(map(int, input().split()))

operator_num = list(map(int, input().split()))

max_val = -1000000001
min_val = 1000000001
q = deque()
q.append((A[0], 1, operator_num))
while q:
    f_num, idx, op_num = q.popleft()
    
    if sum(op_num) == 0:
        if f_num > max_val:
            max_val = f_num
        if f_num < min_val:
            min_val = f_num
        continue
    
    for i in range(4):
        if op_num[i] > 0:
            if i == 0:
                result = f_num + A[idx]
            elif i == 1:
                result = f_num - A[idx]
            elif i == 2:
                result = f_num * A[idx]
            else:
                if f_num < 0:
                    result = -(abs(f_num) // A[idx])
                else:
                    result = f_num // A[idx]
            new_op = op_num.copy()
            new_op[i] -= 1
            q.append((result, idx+1, new_op))
print(max_val)
print(min_val)