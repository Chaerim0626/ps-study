# 0을 어떻게 처리할까? 
def solution(numbers):
    li = [str(s) for s in numbers]

    li.sort(key=lambda x:x*3, reverse=True)
    
    if li[0] == "0":
        return "0"
    return "".join(li)