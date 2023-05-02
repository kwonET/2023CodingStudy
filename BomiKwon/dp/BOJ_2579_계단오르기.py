# 0430 일

n=int(input())
array=[]
for _ in range(n):
  array.append(int(input()))
d=[[] for _ in range(n)]

if n<=2:
  print(sum(array))
else:
  d[0]=(array[0]) #첫번째 계단
  d[1]=(array[1]+array[0]) #두번째 계단
  d[2]=(max(array[2]+array[1],array[2]+d[0]))
  for i in range(3,n):
    d[i]=(max(array[i]+array[i-1]+d[i-3],array[i]+d[i-2]))
  
  print(d[-1])