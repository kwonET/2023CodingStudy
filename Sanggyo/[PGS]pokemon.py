def solution(nums):
    answer = 0
    dic = {}
    for num in nums:
        if num in dic.keys():
            dic[num]+=1
        else:
            dic[num]=1
    
    answer=len(dic.keys())
    if answer>len(nums)/2:
        answer=len(nums)/2
    return answer

