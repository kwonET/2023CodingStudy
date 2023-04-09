# 방향 1) 바뀌는 조건 2) 방향 벡터 선언 주의하기
# 2차원 배열에 위치 + 값으로 해당 위치에 대한 정보 넣는 자료구조를 2개씩 유지.
# 해당 자료구조는 함수로 분리해서 계속 업데이트 가능
# 입출력 시 print("{변수} {변수}".format(변수, 변수))

def change_dir(d):
    if d==1:
        return 2
    if d==2:
        return 1
    if d==3:
        return 4
    if d==4:
        return 3
def move(array):
    # 1. 각 군집들은 1시간마다 이동방향에 있는 다음 셀로 이동한다.
    MAP=[[[] for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if array[y][x]:
                num,d=array[y][x][0]
                ny=y+dy[d]
                nx=x+dx[d]
                # 약품이 칠해진 셀에 도착하면 군집 내 미생물의 절반이 죽고, 이동방향이 반대로 바뀐다.
                if ny==0 or nx==0 or ny==n-1 or nx==n-1:
                    num//=2
                    d=change_dir(d)
                if num>0:
                    MAP[ny][nx].append((num,d))

    for y in range(n):
        for x in range(n):
            if len(MAP[y][x])>=2:
                nm,max_m,max_d=0,0,0
                while MAP[y][x]:
                    _m,_d=MAP[y][x].pop()
                    #군집의 미생물 수는 군집들의 미생물 수의 합
                    nm+=_m
                    # 이동 방향은 군집들 중 미생물 수가 가장 많은 군집의 이동방향
                    if max_m<_m:
                        max_m=_m
                        max_d=_d
                MAP[y][x].append((nm,max_d))
    # 다시 array로 반복할 수 있도록
    return MAP

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dy=[0,-1,1,0,0]
    dx=[0,0,0,-1,1]
    n,m,k=map(int,input().split())
    array=[[[] for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        y,x,num,d=map(int,input().split())
        array[y][x].append((num,d))

    for _ in range(m):
        array=move(array)

    result=0
    for y in range(n):
        for x in range(n):
            while array[y][x]:
                __m,__d=array[y][x].pop()
                result+=__m

    print("#{} {}".format(test_case,result))