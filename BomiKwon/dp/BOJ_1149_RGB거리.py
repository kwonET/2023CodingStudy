n=int(input())
rgb_house=[]
for _ in range(n):
  rgb_house.append(list(map(int,input().split(" "))))

# 각 i번째 집에 대해서, 자기까지 오기까지 최솟값은
# 자기와 다른 색 중에 최솟값 + 지금 집의 값임

for i in range(1,len(rgb_house)):
  rgb_house[i][0]=min(rgb_house[i-1][1],rgb_house[i-1][2])+rgb_house[i][0]
  rgb_house[i][1]=min(rgb_house[i-1][0],rgb_house[i-1][2])+rgb_house[i][1]
  rgb_house[i][2]=min(rgb_house[i-1][0],rgb_house[i-1][1])+rgb_house[i][2]

print(min(rgb_house[len(rgb_house)-1]))