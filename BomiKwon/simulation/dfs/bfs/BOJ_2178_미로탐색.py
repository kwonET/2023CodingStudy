# 전형적인 bfs/dfs 최단경로 문제

from collections import deque

n, m = map(int, input().split(" "))
miro = []
for _ in range(n):
  miro.append(list(map(int, input())))

# r-i-y / c-j-x 좌표 축 헷갈리지 않기
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
  queue = deque()
  queue.append((0, 0))
  while queue:
    y,x = queue.popleft() # popleft 사용
    for i in range(4):
      ny = y + dr[i]
      nx = x + dc[i]
      if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
      if (miro[ny][nx] == 0): continue
      if miro[ny][nx]==1: # 처음 방문한 경우엔 그전까지 온 경로의 합을 더 해줌 -> 다 탐색하지만, 탐색하는 그 값의 출처를 계속 업데이트
        miro[ny][nx] = miro[y][x]+1
        queue.append((ny, nx))
  return miro[n-1][m-1]

print(bfs())
