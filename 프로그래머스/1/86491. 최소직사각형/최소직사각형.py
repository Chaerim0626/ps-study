def solution(sizes):
    result = []
    for a,b in sizes:
        if a>=b:
            result.append([a,b])
        else:
            result.append([b,a])
    min_a, min_b = 0, 0
    print(result)
    for a,b in result:
        min_a = max(a,min_a)
        min_b = max(b,min_b)

    return min_a*min_b