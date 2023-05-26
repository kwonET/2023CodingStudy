# 0517
# 왼 -> 오로 오면서 바로 옆의 칸에서는 못가져오게 함.
result = []

def getScore(array,n):
  for i in range(1,n):
    # 1번 인덱스 : 본인의 값을 저장
    if i==1:
      array[0][i]+=array[1][i-1]
      array[1][i]+=array[0][i-1]
    else:
      # 2번 인덱스 : 왼쪽이 아닌 값 혹은 왼쪽이 아닌 값의 왼쪽 + 본인의 값 저장
      array[0][i]+=max(array[1][i-1],array[1][i-2])
      array[1][i]+=max(array[0][i-1],array[0][i-2])
  return (max(array[0][n-1],array[1][n-1]))
  

tc = int(input())
for _ in range(tc):
  array = []
  n = int(input())
  for _ in range(2):
    array.append(list(map(int, input().split())))
  result.append(getScore(array,n))

for i in result:
  print(i)