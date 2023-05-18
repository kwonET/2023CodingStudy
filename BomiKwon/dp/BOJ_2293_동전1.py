# 0518

n,tv=map(int,input().split(" "))
values=[]
for _ in range(n):
  values.append(int(input()))
values.sort()
#----------------------------
#정답 코드 -> for문을 if문 포함해 간결하게 표현하기 | d에 직접 개수를 넣어줌으로써 2차원 배열로 관리하지 않고 바로 대입하기
#--------------------------
d=[0]*(tv+1)
d[0]=1
for v in values:
  for i in range(v,tv+1):
      d[i]+=d[i-v]

print(d[tv])

#----------------------------
#시간 초과 코드
#--------------------------
# d=[[] for _ in range(tv+1)]
# for v in values:
#   for i in range(v,tv+1):
#     if(i-v<0): continue
#     if(i-v==0): 
#       d[i].append((v,))
#     else: 
#       for j in d[i-v]:
#         new=j+(v,)
#         d[i].append(new)

# print(d)

# print(len(d[tv-1]))