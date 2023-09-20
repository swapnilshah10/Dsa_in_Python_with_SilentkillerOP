# https://www.codingninjas.com/studio/problems/distinct-island_630460

def distinctIsland(grid,n,m) :
    def dfs(i, j, shape):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return

        grid[i][j] = 0  # Mark current cell as visited

        # Add the relative coordinates to the shape
        shape.append((i - start_i, j - start_j))

        # Perform DFS in all four directions
        dfs(i+1, j, shape)
        dfs(i-1, j, shape)
        dfs(i, j+1, shape)
        dfs(i, j-1, shape)

    distinct_shapes = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                shape = []
                start_i, start_j = i, j
                dfs(i, j, shape)
                distinct_shapes.add(tuple(shape))

    return len(distinct_shapes)