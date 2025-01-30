def issafe(grid, x, y, n):
    for row in range(n):
        if grid[row][y] == 1:
            return False
            

    row = x
    col = y
    while row >= 0 and col >= 0:
        if grid[row][col] == 1:
            return False
        row -= 1
        col -= 1
        
    
    row = x
    col = y
    while row >= 0 and col < n:
        if grid[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True

def enqueen(grid, x, n, op):
    if x >= n:
        print(op)
        return
    
    for y in range(n):
        if issafe(grid, x, y, n):
            grid[x][y] = 1
            enqueen(grid, x + 1, n, op + str(x) + str(y) + " ")
            grid[x][y] = 0
            
def nqueen(n):
    if n in [4, 8, 16, 32]:
        grid = [[0] * n for _ in range(n)]  # Initialize grid
        enqueen(grid, 0, n, " ")
    else:
        print("no")

n = int(input())
nqueen(n)
