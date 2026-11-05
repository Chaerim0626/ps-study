def solution(numbers):
    answer = 0
    
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True 
    
    arr = []
    visited = set()
    result = set()
    def backtracking(depth):
        
        if arr:
            result.add(int(''.join(i for i in arr)))
        
        for i in range(len(numbers)):
            if i not in visited:
                visited.add(i)
                arr.append(numbers[i])
                backtracking(depth+1)
                arr.pop()
                visited.remove(i)

    backtracking(0)
    for i in result:
        if is_prime(i):
            answer += 1
            
    return answer