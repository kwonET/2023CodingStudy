#0612 
#1937번
#1520번과 유사한 문제!
#30분 고민 후 비슷한 풀이 참고
import sys
input=sys.stdin.readline
# 1,000,000개의 입력 데이터
sys.setrecursionlimit(10**6)

n=int(input())
array=[]
for _ in range(n):
  array.append(list(map(int,input().split(" "))))

dy=[-1,1,0,0]
dx=[0,0,-1,1]
visited=[[-1]*n for _ in range(n)]

def dfs(y,x):
  if visited[y][x]!=-1: #이미 방문한 적이 있을 땐
    return visited[y][x] #저장된 데이터값
  visited[y][x]=1 #처음 방문 시 1로 초기화
  for i in range(4):
    ny=y+dy[i]
    nx=x+dx[i]
    if (ny<0 or ny>=n or nx<0 or nx>=n): continue
    if array[ny][nx]<=array[y][x]: continue
    visited[y][x]=max(dfs(ny,nx)+1,visited[y][x]) #새 위치까지 도달하는 경우의 수와 이전 위치에서까지 도달하는 경우의 수 중 큰 수로 업데이트
  return visited[y][x]


result=0
for i in range(n):
  for j in range(n):
    result=max(dfs(i,j),result)
print(result)