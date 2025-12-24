from itertools import product

def solution(word):
    answer = 0
    
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []

    for length in range(1, 6):
        for p in product(vowels, repeat=length):
            words.append(''.join(p))

    words.sort()

    return words.index(word) + 1