import bisect,collections,copy,heapq,itertools,math,string,queue
import sys

sys.setrecursionlimit(300000)

N, H = map(int, input().split())
A = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
