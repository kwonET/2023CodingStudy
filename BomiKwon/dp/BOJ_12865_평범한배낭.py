# https://www.youtube.com/watch?v=zRza99HPvkQ&list=PLJULIlvhz0rE83NKhnq7acXYIeA0o1dXb&index=7

n,k=map(int,input().split())
p_w=[]
for _ in range(n):
  p,w=map(int,input().split())
  p_w.append([p,w])
# 무게에 따라 정렬
p_w=sorted(p_w,key=lambda x :x[0])

p=[0]
wt=[0]
for i in range(n):
  wt.append(p_w[i][0]) #가치
  p.append(p_w[i][1]) #무게

# V : 각 짐(i)에 따라 주어진 무게(j) 안에서 넣었을 때 얻을 수 있는 최대 가치(V[i][j])
V=[[[] for _ in range(k+1)] for _ in range(n+1)]
for i in range(n+1):
  for j in range(k+1):
    if i==0 or j==0:
      V[i][j]=0
    elif wt[i]<=j: # 물건의 무게가 주어진 무게 안에 넣을 수 있을 때
      V[i][j]=max(V[i-1][j],V[i-1][j-wt[i]]+p[i])
    else: 
      V[i][j]=V[i-1][j]

# print(V)
print(V[n][k])