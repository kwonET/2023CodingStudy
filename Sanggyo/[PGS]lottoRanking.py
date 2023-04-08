def solution(lottos, win_nums):
    answer = []
    max=7
    min=7
    for i in lottos:
        if i in win_nums:
            min-=1
            max-=1
        else:
            if i == 0:
                max-=1
    if (max>6):
        max=6
    if (min>6):
        min=6
    answer.append(max)
    answer.append(min)
    return answer