#0529 
#이어진 경로가 여러개인 경우엔, 따로 탐색한다는 개념으로 접근한다.
#방문여부와 집의 유무를 잘 구분해 처리하는 게 관건인 문제.
from collections import deque

n = int(input())
array = []
for i in range(n):
  array.append(list(map(int, input())))
# 방향 벡터
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 집이 있는 위치를 담은 배열
house = []
for i in range(n):
  for j in range(n):
    if array[i][j] == 1:
      house.append((i, j))

# 단지 유무를 판단하는 bfs함수
def bfs(i, j):
  queue = deque()
  queue.append((i, j))
  result=0
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
      if array[ny][nx] == 0: continue
      if array[ny][nx] == 1:
        array[ny][nx] =array[y][x]
        queue.append((ny, nx))
        result+=1
  # 만약 단지에 집이 1개일 경우 따로 처리해서 출력
  if result==0:
    return 1
  # 그 외엔 계산된 값을 출력
  else:
    return result

# 집이 있는 곳을 시작점으로 지정해서 탐색
house_num = []
for h in house:
  i, j = h
  if array[i][j] == 1:
    house_num.append(bfs(i, j))
    
house_num.sort() #오름차순
#답 출력
print(len(house_num))
for answer in house_num:
  print(answer)

