#0611
m, n = map(int, input().split(" "))  #세로, 가로
array = []
for _ in range(m):
  array.append(list(map(int, input().split(" "))))
#방향벡터
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
#bfs 수행하고, 각 지점에서 목표 지점으로 갈 수 있는 경우의 수를 각 위치에 저장
visited = [[-1] * n for _ in range(m)]


def dfs(y, x):
  #종료 조건
  #1) 도착지점에 도달한 경우 
  if (y == m - 1 and x == n - 1):
    return 1
  #2) 저장되어 있는 경우
  # 저장된 '그 위치에서 출발해서 도달가능한 수'를 반환
  if visited[y][x] != -1:
    return visited[y][x]
    
  #탐색 조건
  new=0
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
    if array[ny][nx] >= array[y][x]: continue
    #재귀로 갈 수 있는 데까지 깊이 우선 탐색 후, 해당 위치에 저장된 값을 return으로 전달
    new+=dfs(ny,nx)
    
  #return 값
  visited[y][x]=new
  print(new)
  return visited[y][x]
  
print(dfs(0,0))
# print(visited)