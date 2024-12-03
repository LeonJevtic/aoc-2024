def is_safe(report):
    increasing = all(1 <= report[i+1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i+1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

with open("day_02.in") as fin:
    data = fin.read()

ans = 0
for line in data.strip().split("\n"):
    levels = [int(i) for i in line.split()]
    if is_safe(levels):
        ans += 1

print(ans)