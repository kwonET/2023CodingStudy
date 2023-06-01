#0527
#참고 : https://jyeonnyang2.tistory.com/51 | https://hongcoding.tistory.com/84
n=int(input())
d=[0] *(n+1)

#0과 그 외 홀수는 0으로 출력
if n%2!=0:
  print(0)
#짝수에 대해서만 성립
else:
  d[2]=3
  for i in range(4,n+1,2):
    # 1) d[i-2]*3 : 세로가 n-2와 2로 나뉠 때 d[2]=3 : 끝에 3가지 조합을 붙여주는 경우
    # 2) 2 : 상관없이 생기는 특수한 2개의 타일 조합
    d[i]=d[i-2]*3+2
    # 3)  d[i-4]*2 + d[i-6]*2 + ... + d[2]*2 : 끝에 고유한 모양을 붙여주는 경우
    for j in range(2,i-2,2):
      d[i]+=d[j]*2
  
  print(d[n])


