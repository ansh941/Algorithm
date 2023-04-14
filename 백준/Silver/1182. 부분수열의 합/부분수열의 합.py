N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
def part_sequence(index, s, flag = False):
    global count
    if index == N:
        if s == S and flag:
            count += 1
        return
    part_sequence(index+1, s, flag or False)
    part_sequence(index+1, s+nums[index], True)
    
part_sequence(0, 0, False)
print(count)

