import math

most_powerful_word = ''
score = 0
list_of_vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
best_score = 0
while True:
    word = input()
    if word == 'End of words':
        break

    for char in word:
        score += ord(char)

    if word[0] in list_of_vowels:
        score *= len(word)
    else:
        score /= len(word)
        score = math.floor(score)

    if score >= best_score:
        best_score = score
        most_powerful_word = word
    score = 0

print(f'The most powerful word is {most_powerful_word} - {best_score}')
