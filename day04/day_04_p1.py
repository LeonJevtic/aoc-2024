def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1)
    ]

    def is_valid_my_g(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid_my_g(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_word(i, j, dx, dy):
                    count += 1
                if check_word(i, j, -dx, -dy):
                    count += 1

    return count

with open("day_04.in") as fin:
    grid = [line.strip() for line in fin]

result_or_smth_like_that = count_xmas(grid)
print(result_or_smth_like_that)