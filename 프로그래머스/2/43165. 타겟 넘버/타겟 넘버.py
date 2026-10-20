def solution(numbers, target):
    answer = 0

    def dfs(index,cur_num):
        nonlocal answer 
        
        if index == len(numbers):
            if cur_num == target:
                answer += 1
            return 
        
        dfs(index+1,cur_num+numbers[index])
        dfs(index+1,cur_num-numbers[index])
     
    dfs(0,0)
        
    return answer