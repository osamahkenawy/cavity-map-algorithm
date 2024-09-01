n = 4
grid = [
    "1112",
    "1912",
    "1892",
    "1234"
]

def cavityMap(grid):
    n = len(grid)
    grid = [list(row) for row in grid]
    for i in range(1, n - 1):  
        for j in range(1, n - 1): 
            current = grid[i][j]
            top = grid[i-1][j]
            bottom = grid[i+1][j]
            left = grid[i][j-1]
            right = grid[i][j+1]

            if current > top and current > bottom and current > left and current > right:
                grid[i][j] = 'X'
    return [''.join(row) for row in grid]

result = cavityMap(grid)
for row in result:
    print(row)