import re

with open("day03/day_03.in") as fin:
    data = fin.read()
    
ans = 0

pattern = r'mul\(\d{1,3},\d{1,3}\)'

matches = re.findall(pattern, data)

ans = 0

for match in matches:
    numbers = re.findall(r'\d{1,3}', match)
    x, y = int(numbers[0]), int(numbers[1])
    
    ans += x * y

print(ans)