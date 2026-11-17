def solution(word):
    s = []
    w = []
    alpha = 'AEIOU'
    
    def backtracking(start):
        if len(w) == 5:
            return 
        
        for i in range(5):
            w.append(alpha[i])
            if ''.join(w) not in s:
                s.append(''.join(w))
            backtracking(start+1)
            w.pop()
            
    backtracking(0)
    return s.index(word) + 1