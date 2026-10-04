def solution(code):
    mode = 0
    ret = ''
    length = len(code)
    
    for i in range(length):
        if not mode:
            if code[i] != '1':
                if i % 2 == 0:
                    ret += code[i]
            else:
                mode = 1
        else:
            if code[i] != '1':    
                if i % 2 == 1:
                    ret += code[i]
            else:
                mode = 0

    return ret if ret != '' else 'EMPTY'