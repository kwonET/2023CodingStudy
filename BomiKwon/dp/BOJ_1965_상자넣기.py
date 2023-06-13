#0613 #1965번
# https://www.acmicpc.net/problem/11055 와 유사하다고!

n = int(input())
array = list(map(int, input().split()))
d = [1] * n
for i in range(1, n):
  for j in range(i):
    #나보다 작은 수에 대해 1번부터 다 판단
    if (array[i] > array[j]):
      #내가 가진 값(j보다 더 작은 값)보다 더 큰 값이 있을 경우 업데이트
      d[i] = max(d[i], d[j] + 1)

print(max(d))
