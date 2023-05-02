# 0. k번 실행 하기 전 모두 탈출했을 때를 대비해 탈출여부를 확인하는 함수
def fin(array):
    for y in range(n):
        for x in range(n):
            if len(array[y][x])>0:
                return False
    return True

# 0. 출구를 계속해서 업데이트하는 함수
def exit(array):
    for y in range(n):
        for x in range(n):
            if array[y][x]==[-1]:
                return (y,x)

# 1. 이동
def move(array):
    global total_move_dist
    #상하좌우로 움직일 수 있으며,
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    #모든 참가자는 동시에 움직입니다.
    MAP=[[[] for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            #움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
            min_dist,min_y,min_x=abs(y-ey)+abs(x-ex),y,x
            while array[y][x]:
                explorer=array[y][x].pop()
                #움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
                for d in range(4):
                    ny=y+dy[d]
                    nx=x+dx[d]
                    #참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다. - 범위 초과
                    if ny<0 or ny>=n or nx<0 or nx>=n : continue
                    #벽이 없는 곳으로 이동할 수 있습니다.
                    if wall[ny][nx]>0: continue
                    #두 위치 (x1,y1), (x2,y2)의 최단거리는 ∣x1−x2∣+∣y1−y2∣로 정의됩니다.
                    dist=abs(ny-ey)+abs(nx-ex)
                    if min_dist>dist:
                        min_dist=dist
                        min_y=ny
                        min_x=nx
                if min_y!=y or min_x!=x:
                    total_move_dist+=1
                if min_y==ey and min_x==ex: continue
                #한 칸에 2명 이상의 모험가가 있을 수 있습니다.
                MAP[min_y][min_x].append(explorer)
    return MAP

# 0. 정사각형을 찾아 위치와 길이를 반환하는 함수
def square(array):
# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
# 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
    for leng in range(2,n+1):
        for y in range(n-leng+1):
            for x in range(n-leng+1):
                # i,j ~ i+x,j+x까지를 확인
                flag=[0,0]
                for i in range(leng):
                    for j in range(leng):
                        if array[y+i][x+j]==[-1]:
                            flag[0]=1
                        elif len(array[y+i][x+j])>0:
                            flag[1]=1
                if flag==[1,1]: return y,x,leng


# 2. 회전
def rotate():
# 선택된 정사각형은 시계방향으로 90도 회전하며, 
    n,m,l=square(array)
    MAP=[[[] for _ in range(l)] for _ in range(l)]
    for y in range(n,n+l):
        for x in range(m,m+l):
            MAP[x-m][l+n-y-1]=array[y][x]
    # print("MAP")
    # print(MAP)
    for y in range(n,n+l):
        for x in range(m,m+l):
            array[y][x]=MAP[y-n][x-m]

    # 회전된 벽은 내구도가 1씩 깎입니다.
    WALL=[[0]*l for _ in range(l)]
    for y in range(n,n+l):
        for x in range(m,m+l):
            if wall[y][x]>0:
                WALL[x-m][l+n-y-1]=wall[y][x]-1
    # print("WALL")
    # print(WALL)
    for y in range(n,n+l):
        for x in range(m,m+l):
            wall[y][x]=WALL[y-n][x-m]


# n 미로의 크기 m 참가자 수  k 게임 시간
n,m,k = map(int,input().split())
wall=[]
for _ in range(n):
    wall.append(list(map(int,input().split())))
array=[[[] for _ in range(n)] for _ in range(n)]
for i in range(1,m+2):
    r,c=map(int,input().split())
    r-=1
    c-=1
    if i==m+1:
        array[r][c].append(-1) # 출구
        break
    array[r][c].append(i) #모험가의 id를 저장해놓음
    
total_move_dist=0
fin_flag=0

# 실행시간 k동안 실행
for kk in range(k):
    ey,ex=exit(array)
    array=move(array)
    # 이동 후 모두 탈출한 경우
    if fin(array):
        print(total_move_dist)
        print(ey+1,ex+1)
        fin_flag=1
        break
    array[ey][ex]=[-1]
    rotate()
    
if fin_flag==0:
    ey,ex=exit(array)
    print(total_move_dist)
    print(ey+1,ex+1)