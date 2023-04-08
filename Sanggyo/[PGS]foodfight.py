import math
def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        answer+=str(i)*math.floor(food[i]/2)
    
    res = answer+"0"+answer[::-1]
    return res
