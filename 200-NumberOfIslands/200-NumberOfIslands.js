// Last updated: 3/1/2026, 11:44:36 PM
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {

    //base case
    if (grid.length === 0) return

    let count = 0

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === "1") {
                count += 1
                dfs(grid, i, j)
            }
        }
    } return count
};

var dfs = function (grid, row, col) {
    // out of bounds exception
    if(row < 0 || col < 0 || row >= grid.length || col >=grid[0].length) return 0

    // return if water
    if(grid[row][col] === "0") return

    // mark visited by turning land to water
    grid[row][col] = "0"

    dfs(grid, row-1, col)
    dfs(grid, row+1, col)
    dfs(grid, row, col-1)
    dfs(grid, row, col+1)
}