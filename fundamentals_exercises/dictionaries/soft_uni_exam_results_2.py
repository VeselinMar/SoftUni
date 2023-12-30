def update_user(dictionary: dict, user: str, lang: str, score: int):
    global submissions
    if user not in dictionary:
        dictionary[user] = {lang: score}
        if lang not in submissions:
            submissions[lang] = 1
        else:
            submissions[lang] += 1
    else:
        if lang not in dictionary[user]:
            dictionary[user][lang] = score
            if lang not in submissions:
                submissions[lang] = 1
            else:
                submissions[lang] += 1
        else:
            submissions[lang] += 1
            if dictionary[user][lang] < score:
                dictionary[user][lang] = score


submissions = {}
exam_results = {}
line = input()
while line != 'exam finished':
    if 'banned' in line:
        username, ban = line.split('-')
        for language in exam_results[username]:
            exam_results[username][language] = 0
        line = input()
    else:
        username, language, points = line.split('-')
        update_user(exam_results, username, language, int(points))
        line = input()

print('Results:')
for name, results in exam_results.items():
    total_score = sum(results.values())
    if total_score > 0:
        print(f'{name} | {total_score}')

print('Submissions:')
for lang, result in submissions.items():
    if result > 0:
        print(f'{lang} - {result}')
