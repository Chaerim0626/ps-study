def solution(skill, skill_trees):
    answer = 0
    
    def solve(s,skill):
        tmp = ''
        for i in range(len(s)):
            if s[i] in skill:
                tmp += s[i]

        if skill.startswith(tmp):
            return True
        else:
            return False
    
    for i in skill_trees:
        if solve(i,skill):
            answer += 1
    
    return answer