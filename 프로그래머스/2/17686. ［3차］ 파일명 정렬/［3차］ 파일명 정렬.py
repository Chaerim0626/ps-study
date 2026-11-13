def solution(files):
    answer = []
    new_files = []
    
    for i, file in enumerate(files):
        idx = 0
        head,num = '', ''
        
        while idx < len(file) and not file[idx].isdigit():
            head += file[idx]
            idx += 1
        
        while idx < len(file) and file[idx].isdigit():
            num += file[idx]
            idx += 1
        
        new_files.append((i,head.lower(),int(str(num[:5]))))
        new_files.sort(key=lambda x:(x[1],x[2],x[0]))       

    for i in new_files:
        answer.append(files[i[0]])

    return answer