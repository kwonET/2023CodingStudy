# 깨달은 점 
# '동시에' 라는 워딩 조심하기. 또다른 자료구조 만들어서 관리해주기
# 2차원 빈 배열의 배열을 만들어서 중간 값을 계산해서 저장해주기
# 배열 선언/변경 보다 'while문과 pop(), append()'를 적절히 사용해서 시간초과 방지하기
# 문항 꼼꼼히 읽고 확인하기.

n, m, k = map(int, input().split())
fireball = []
for _ in range(m):
    fireball.append(list(map(int, input().split())))

# 방향 벡터
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)

for f in fireball:
    f[0] -= 1
    f[1] -= 1

MAP=[[[] for _ in range(n)] for _ in range(n)]

for _ in range(k):
    # 1) 파이어볼 이동
    while fireball:
        r, c, m, s, d = fireball.pop()
        r = (r + dy[d] * s) % n
        c = (c + dx[d] * s) % n
        MAP[r][c].append([m,s,d])

    # 2) 2개 이상의 파이어볼 분리
    for y in range(n):
        for x in range(n):
            if len(MAP[y][x])>=2:
                nm,ns,nd,cnt=0,0,0,len(MAP[y][x])
                while MAP[y][x]:
                    _m,_s,_d=MAP[y][x].pop()
                    nm+=_m
                    ns+=_s
                    if _d%2==0:
                        nd+=1
                    elif _d%2==1:
                        nd+=-1
                if nd==cnt or nd==-cnt:
                    if nm//5!=0:
                        for i in range(4):
                            fireball.append([y,x,nm//5,ns//cnt,i*2])
                else:
                    if nm // 5 != 0:
                        for i in range(4):
                            fireball.append([y,x,nm//5,ns//cnt,i*2+1])

            if len(MAP[y][x])==1:
                fireball.append([y, x]+ MAP[y][x].pop())

    # print(fireball)
    # print('-----------')
print(sum(f[2] for f in fireball))