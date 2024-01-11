country_names = input().split(', ')
capital_names = input().split(', ')

pairs = {}

for pair in range(len(country_names)):
    key, value = country_names[pair], capital_names[pair]
    pairs[key] = value

for key, value in pairs.items():
    print(f'{key} -> {value}')
