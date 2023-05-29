#0528 DP 
#왜 다이나믹 프로그래밍인가?
#-> 그 전에 거쳐온 경로의 값을 기억하고, 뒤의 더 큰 문제에 이용한다.
#-> 또한 우리는 마지막에 몇 번의 경우의 수를 통해 도착했는지를 알아내야 하기 때문에
#-> dfs/bfs로 모든 탐색 경로를 지정하는 것이 아닌, dp를 통해 지나온 흐름을 기록하기만 하면 된다.

n=int(input())
array=[]
for y in range(n):
  array.append(list(map(int,input().split(" "))))

#방향벡터
dy=[0,1]
dx=[1,0]
#거쳐온 array의 위치를 기록하는 자료구조
d=[[0] *n for _ in range(n)]
d[0][0]=1

#array배열에서 d를 갱신하는 함수
def find():
  for y in range(n):
    for x in range(n):
      if y==n-1 and x==n-1: #맨 오른쪽 아래에 도착
        return d[y][x]
      weight=array[y][x]
      for i in range(2):
        ny=y+dy[i]*weight
        nx=x+dx[i]*weight
        #범위가 벗어나지 않으면 거쳐갈 수 있음.
        if ny>=n or nx>=n: continue
        d[ny][nx]+=d[y][x]

print(find())