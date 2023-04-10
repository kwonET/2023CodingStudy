def solution(phone_book):
    answer = True
    length=len(phone_book)
    
    phone_book.sort() 
    for i in range(length-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer=False
            return answer
        
    return answer