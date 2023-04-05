# 배열의 시작이 1일 때 -> 주어진 값만 -1 해서 0으로 초기화하기
# y-r-i / x-c-j 헷갈리지 않고 배열 값 넣기
# 방향벡터 튜플+for문으로 잘 사용하기

import sys
n,m=map(int,sys.stdin.readline().split())
array=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
move=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]


# 8 방향
dy8=(0,-1,-1,-1,0,1,1,1)
dx8=(-1,-1,0,1,1,1,0,-1)
# 4 방향
dy4=(-1,1,-1,1)
dx4=(-1,1,1,-1)
# 초기 구름 위치
clouds=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
                                 
# 각 이동/ 방향 지시에 대해
for d,s in move:
  # 1) 이동
  # 각 구름 위치마다 이동
  move_clouds=[]
  for r,c in clouds:
    ny=(r+dy8[d-1]*s)%n
    nx=(c+dx8[d-1]*s)%n
    array[ny][nx]+=1
    move_clouds.append((ny,nx))
  
  #3) 각 구름의 대각선에 대해 확인
  for r,c in move_clouds:
    cnt=0
    for i in range(4):
      ny=r+dy4[i]
      nx=c+dx4[i]
      if nx<0 or nx>=n or ny<0 or ny>=n: continue
      if array[ny][nx]!=0: cnt+=1
    array[r][c]+=cnt
    
  n_clouds=[]
  #4) 새로운 구름 위치 설정
  for y in range(n):
    for x in range(n):
      if (y,x) in move_clouds or array[y][x]<2: continue
      array[y][x]-=2
      n_clouds.append((y,x))
  clouds=n_clouds

#5) 결과 출력
result=0
for y in range(n):
  for x in range(n):
    result+=array[y][x]
print(result)