uniques = set()
sentence = input()

for symbol in sentence:
    uniques.add(symbol)

for symbol in sorted(uniques):
    print(f'{symbol}: {sentence.count(symbol)} time/s')
