def solution(n):
    answer = 0
    path = []
    
    def backtracking(depth):
        nonlocal answer 
        if depth == n:
            answer += 1
            return 

        for i in range(n):
            if i not in path:
                
                is_diagonal = False
                for row in range(depth):
                    if abs(path[row] - i) == depth - row:
                        is_diagonal = True
                if is_diagonal:
                    continue 
                    
                path.append(i)
                backtracking(depth+1)
                path.pop()
    
    backtracking(0)
    return answer