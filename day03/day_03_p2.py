import re

def func(input_string):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    instruction_pattern = r"do\(\)|don't\(\)"

    mul_matches = list(re.finditer(mul_pattern, input_string))
    instructions = list(re.finditer(instruction_pattern, input_string))

    is_enabled = True
    mul_results = []
    instruction_index = 0

    for mul in mul_matches:
        while instruction_index < len(instructions) and instructions[instruction_index].start() < mul.start():
            instruction_text = instructions[instruction_index].group()
            if instruction_text == "do()":
                is_enabled = True
            elif instruction_text == "don't()":
                is_enabled = False
            instruction_index += 1

        if is_enabled:
            a, b = map(int, mul.groups())
            mul_results.append(a * b)

    return sum(mul_results)

with open("day03/day_03.in") as fin:
    data = fin.read().strip()
print(func(data))
