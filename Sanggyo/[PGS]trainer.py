def solution(n, lost, reserve):
    dic={}
    answer = 0
    
    for i in range(1,n+1):
        dic[i]=1
        
    for item in lost:
        dic[item]-=1
        
    for item in reserve:
        dic[item]+=1
    
    for key, value in dic.items():
        if value==0:
            if key==1:
                if dic[key+1]==2:
                    dic[key+1]-=1
                    dic[key]+=1
            elif key==n:
                if dic[key-1]==2:
                    dic[key-1]-=1
                    dic[key]+=1
            else:
                if dic[key-1]==2:
                    dic[key-1]-=1
                    dic[key]+=1
                elif dic[key+1]==2:
                    dic[key+1]-=1
                    dic[key]+=1
    for key, value in dic.items():
        if value>=1:
            answer+=1
    return answer