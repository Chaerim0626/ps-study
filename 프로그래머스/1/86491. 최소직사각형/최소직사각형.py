def solution(sizes):
    answer = 0
    
    new_sizes = []
    sizes.sort(key=lambda x:(x[0],x[1]))

    for i,j in sizes:
        if i >= j:
            new_sizes.append([i,j])
        else:
            new_sizes.append([j,i])
    
    new_sizes.sort(reverse=True)

    max_i,max_j = 0,0
    for i, j in new_sizes:
        max_i,max_j = max(max_i,i), max(max_j,j)
        
    return max_i*max_j