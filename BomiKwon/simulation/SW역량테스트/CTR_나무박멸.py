# 나무 성장 / 번식 칸과 제초제 칸을 구분해서 자료구조 관리하기
# 헷갈리는 경우 함수로 관리하면 이해가 편하다
# 최대/최소 함수 내에서 업데이트하는 거 이해하기

n, m, k, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
herb=[[0]*n for _ in range(n)] # 제초제를 관리하는 자료구조
ans=0
visited = [[0] * n for _ in range(n)]

def step_one():
    # 1. 나무의 성장
    # 1) 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다.
    dy1 = [-1, 0, 1, 0]
    dx1 = [0, 1, 0, -1]
    for y in range(n):
        for x in range(n):
            # 나무가 있는 칸에 대해
            if array[y][x]<1: continue

            # 나무가 있는 칸의 수만큼 나무가 성장
            cnt=0
            for d in range(4):
                ny = y + dy1[d]
                nx = x + dx1[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if array[ny][nx]>0:
                    cnt+=1
            array[y][x] += cnt

def step_two():
    dy1 = [-1, 0, 1, 0]
    dx1 = [0, 1, 0, -1]
    # 2. 나무의 번식
    # 2) 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행합니다.

    # 동시에 번식하는 것을 구현하기 위한 자료구조
    for y in range(n):
        for x in range(n):
            visited[y][x]=0

    for y in range(n):
        for x in range(n):
            if array[y][x]<1: continue

            # 이때 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수을 찾는다
            cnt=0
            for d in range(4):
                ny = y + dy1[d]
                nx = x + dx1[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if herb[ny][nx]: continue
                if array[ny][nx] == 0:
                    cnt+=1

            # 인접한 나무들 위치에 아무도 없는 개수만큼 나눠준 몫을 번식시킨다
            for d in range(4):
                ny = y + dy1[d]
                nx = x + dx1[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
                if herb[ny][nx]: continue
                if array[ny][nx] == 0:
                    visited[ny][nx]+=array[y][x]//cnt

    # 번식의 과정은 모든 나무에서 동시에 일어나게 됩니다.
    for y in range(n):
        for x in range(n):
            array[y][x]+=visited[y][x]


# 3. 제초제를 뿌릴 위치 선정
# 각 칸 중 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
def step_three():
    global ans # 정답

    dy2 = [-1, 1, 1, -1]
    dx2 = [1, 1, -1, -1]
    max_del, max_y, max_x=0,0,0
    for y in range(n):
        for x in range(n):
            if array[y][x]<1: continue

            cnt=array[y][x]
            # 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만,
            # 나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.
            for d in range(4):
                for i in range(1, k + 1):
                    ny = y + dy2[d] * i
                    nx = x + dx2[d] * i
                    # 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 
                    # 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
                    if nx < 0 or nx >= n or ny < 0 or ny >= n: break
                    if array[ny][nx]<1: break
                    cnt += array[ny][nx]

            # 각 나무마다 최댓값을 비교해서 갱신
            if max_del<cnt:
                max_del,max_y,max_x=cnt,y,x
    ans+=max_del


    if array[max_y][max_x]>0:
        array[max_y][max_x]=0
        herb[max_y][max_x]=c
        for d in range(4):
            for i in range(1, k + 1):
                ny = max_y + dy2[d] * i
                nx = max_x + dx2[d] * i
                if nx < 0 or nx >= n or ny < 0 or ny >= n: break
                # 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
                if array[ny][nx] < 0: break
                if array[ny][nx]==0:
                    herb[ny][nx]=c
                    break
                array[ny][nx]=0
                herb[ny][nx]=c


def delete_herb():
    for y in range(n):
        for x in range(n):
            if herb[y][x]>0:
                herb[y][x]-=1


for _ in range(m):
    step_one()
    # print(array)
    step_two()
    # print(array)

    # 제초제 기간을 감소
    delete_herb()
    step_three()
    # print(array)
    # print('--------------')
print(ans)