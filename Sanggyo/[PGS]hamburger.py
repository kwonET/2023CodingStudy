def solution(ingredient):
    answer = 0
    s=[]
    for n in ingredient:
        s.append(n)
        if s[-4:] == [1,2,3,1]:
            answer+=1
            for _ in range(4):
                s.pop()
    return answer