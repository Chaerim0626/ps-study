def solution(numbers, target):
    answer = 0
    
    def dfs(index, cur_sum):
        nonlocal answer  
        
        # 1. 종료 조건: 모든 숫자를 다 사용했을 때
        if index == len(numbers):  # 뭘 써야 할까요?
            if cur_sum == target:  # 무엇과 비교해야 할까요?
                answer += 1
            return
        
        # 2. 현재 숫자를 더하는 경우
        dfs(index+1, cur_sum+numbers[index]) 
        dfs(index+1, cur_sum-numbers[index])  
        
    dfs(0, 0)  # 0번째 인덱스부터 시작, 초기 합 0
    return answer