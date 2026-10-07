def solution(today, terms, privacies):
    answer = []
    dic = dict()
    # ['2019.01.01 D', '2019.11.15 Z']
    # 파기해야할 개인정보 번호를 오름차순 1차원 정수 배열에 담아 return 
    year,month,date = today.split('.')
    days = int(date) + int(month)*28 + int(year)*12*28
    arr= []
    for i in range(len(privacies)):
        idx = i+1
        d,alpha =privacies[i].split(' ')
        arr.append((idx,d,alpha))
        
    for i in range(len(terms)):
        a,b = terms[i].split(' ')
        dic[a] = b
    
    for i in range(len(arr)):
        y,m,d = arr[i][1].split('.')
        m = int(m) + int(dic[arr[i][2]])
        y,m,d = int(y),int(m),int(d)
        tmp = d + m*28 + y*12*28
        
        if days >= tmp:
            answer.append(arr[i][0])
        
    return answer