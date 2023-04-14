# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:10:39 2021

@author: ASH
"""

#import sys
from queue import Queue

#sys.stdin = open("input.txt", "r")

# N: 세로 M: 가로
#N, M = map(int, sys.stdin.readline().split())
N, M = map(int, input().split())

board = []
for i in range(N):
    #tmp = sys.stdin.readline()
    tmp = input()
    tmp = ' '.join(tmp).split()
    board.append(tmp)
    
class INFO:
    def __init__(self, ry, rx, by, bx, count):
        self.ry = ry
        self.rx = rx
        self.by = by
        self.bx = bx
        self.count = count
    
    def __str__(self):
        return 'INFO({}, {}, {}, {}, {})'.format(self.ry, self.rx, self.by, self.bx, self.count)

def bfs():
    # 좌표 이동 값(상 하 좌 우)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    visited = [[[[0 for i in range(10)] for j in range(10)] for k in range(10)] for l in range(10)]
    q = Queue()
    q.put(start)
    visited[start.ry][start.rx][start.by][start.bx] = 1
    
    ret = -1
    while not q.empty():
        cur = q.get()
        
        if cur.count > 10:
            break
        if board[cur.ry][cur.rx] =='O' and board[cur.by][cur.bx] != 'O':
            ret = cur.count
            break
        
        for direction in range(4):
            next_ry = cur.ry
            next_rx = cur.rx
            next_by = cur.by
            next_bx = cur.bx
            
            while True:
                if board[next_ry][next_rx] != '#' and board[next_ry][next_rx] != 'O':
                    next_ry += dy[direction]
                    next_rx += dx[direction]
                else:
                    if board[next_ry][next_rx] == '#':
                        next_ry -= dy[direction]
                        next_rx -= dx[direction]
                    break
            while True:
                if board[next_by][next_bx] != '#' and board[next_by][next_bx] != 'O':
                    next_by += dy[direction]
                    next_bx += dx[direction]
                else:
                    if board[next_by][next_bx] == '#':
                        next_by -= dy[direction]
                        next_bx -= dx[direction]
                    break
            
            if next_ry == next_by and next_rx == next_bx:
                if board[next_ry][next_rx] != 'O':
                    red_dist = abs(next_ry-cur.ry) + abs(next_rx - cur.rx)
                    blue_dist = abs(next_by-cur.by) + abs(next_bx - cur.bx)
                    if red_dist > blue_dist:
                        next_ry -= dy[direction]
                        next_rx -= dx[direction]
                    else:
                        next_by -= dy[direction]
                        next_bx -= dx[direction]
            
            if visited[next_ry][next_rx][next_by][next_bx] == 0:
                visited[next_ry][next_rx][next_by][next_bx] = 1
                n = INFO(next_ry, next_rx, next_by, next_bx, cur.count+1)
                q.put(n)
    return ret
    
# 시작 위치 찾기
start = INFO(0,0,0,0,0)
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            start.ry = i
            start.rx = j
        if board[i][j] == 'B':
            start.by = i
            start.bx = j

ret = bfs()
print(ret)
