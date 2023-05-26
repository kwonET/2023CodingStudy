#0526

n, k = map(int, input().split(" "))
value = []
for _ in range(n):
  value.append(int(input()))
value.sort()

d = [-1] * (k + 1)
d[0] = 0 # 0번째 인덱스는 0으로 지정
for v in value:
  for i in range(v, k + 1):
    if d[i - v] != -1:
      if d[i] != -1: #만약 이전에 값이 지정되었으면
        d[i] = min(d[i - v] + 1, d[i])
      else: # 처음 지정되는 경우라면
        d[i] = d[i - v] + 1

# print(d)
print(d[k])
