from histogram_filter.helpers import normalize, blur


def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs


def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []

    for r in range(len(grid)):
        row = []

        for c in range(len(grid[r])):
            if grid[r][c] == color:
                v = beliefs[r][c] * p_hit
            else:
                v = beliefs[r][c] * p_miss

            row.append(v)

        new_beliefs.append(row)

    return normalize(new_beliefs)


def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for _ in range(width)] for _ in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            # pdb.set_trace()
            new_G[new_i][new_j] = cell

    return blur(new_G, blurring)
