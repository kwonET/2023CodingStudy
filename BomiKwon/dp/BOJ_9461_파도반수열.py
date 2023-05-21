#0521
t=int(input())
result=[]
for _ in range(t):
  n=int(input())
  d=[0]*n
  for i in range(n):
    if(i<3):
      d[i]=1
    elif i<5:
      d[i]=2
    else: # 5 이상부터 점화식을 따른다
      d[i]=d[i-1]+d[i-5]
  result.append(d[n-1])

for r in result:
  print(r)
    