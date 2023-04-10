def solution(participant, completion):
    answer = ''
    dic={}
    for man in participant:
        if man in dic.keys():
            dic[man]+=1
        else:
            dic[man]=1
    for man in completion:
        dic[man]-=1
    
    for i in dic.items():
        if i[1] != 0:
            answer=i[0]
        
    return answer

