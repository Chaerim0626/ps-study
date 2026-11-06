def solution(n, lost, reserve):
    # 바로 앞이나 뒤에만 빌릴 수 있음 
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for r in sorted(real_reserve):
        if r-1 in real_lost:
            real_lost.remove(r-1)
        elif r+1 in real_lost:
            real_lost.remove(r+1)

    return n-len(real_lost)