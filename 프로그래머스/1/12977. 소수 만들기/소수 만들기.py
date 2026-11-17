from itertools import combinations 
def solution(nums):
    answer = 0
    coms = list(combinations(nums,3))
    
    def is_prime(n):
        if n == 1:
            return False 
        
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True 
    
    for com in coms:
        if is_prime(com[0]+com[1]+com[2]):
            answer += 1

    return answer