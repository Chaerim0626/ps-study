def solution(s):
    answer = ''
    words = s.split(' ')
    print(words)
    
    new_words = []
    for word in words:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        
        new_words.append(new_word)
        
    return ' '.join(new_words)