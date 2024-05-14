class Solution {
    public int numIslands(char[][] grid) {
        int numberIslands = 2;

        for (int x = 0; x < grid.length; x++) {
            for (int y = 0; y < grid[0].length; y++) {
                if(grid[x][y] == '1'){
                    changeAdjacent(grid, x, y, numberIslands);
                    numberIslands++;
                }
            }
        }
        return numberIslands - 2;
    }

    private void changeAdjacent(char[][] grid, int x, int y, int currentIsland){
        if(grid[x][y] == '1'){
            grid[x][y] = (char)(currentIsland+'0');
            if(x - 1 >= 0){
                changeAdjacent(grid, x -1, y, currentIsland);
            }
            if(x + 1 < grid.length){
                changeAdjacent(grid, x +1, y, currentIsland);
            }
            if(y - 1 >= 0){
                changeAdjacent(grid, x, y-1, currentIsland);
            }
            if(y + 1 < grid[0].length){
                changeAdjacent(grid, x, y+1, currentIsland);
            }
        }else{
            return;
        }
    }
}

