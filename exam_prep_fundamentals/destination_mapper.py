import re

destinations = input()

pattern = r'=[A-Z][A-Za-z]{2,}=|\/[A-Z][A-Za-z]{2,}\/'

matches = re.findall(pattern, destinations)

# Remove '=' or '/' symbols and calculate travel points
cleaned_destinations = [re.sub(r'[^A-Za-z]', '', match) for match in matches]
travel_points = sum(len(cleaned) for cleaned in cleaned_destinations)

print(f"Destinations: {', '.join(cleaned_destinations)}")
print(f"Travel Points: {travel_points}")
