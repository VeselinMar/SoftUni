country_names = input().split(', ')
capital_names = input().split(', ')

pairs = zip(country_names, capital_names)

for country_names, capital_names in pairs:
    print(f'{country_names} -> {capital_names}')
