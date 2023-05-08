# 긴 변, 중간 변, 작은 변으로 만들기 (for문과 break 활용)
# 긴 변 < 중간 + 작은 변 => 삼각형 수식 성립 여부 판단하기

n = int(input())
result = 0
for a in range(1,n): #가장 짧은 변
  for b in range(a,n): 
    c=n-(a+b)
    if (b>c):  break #c가 가장 길도록, 중복 제거
    if (b+a>c): result+=1
    
print(result)
