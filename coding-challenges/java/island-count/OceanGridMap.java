class OceanGridMap {
    public boolean[][] grid;

    public OceanGridMap(boolean[][] grid) {
        this.grid = grid;
    }

    public static int countIslands(OceanGridMap oceanMap) {
        int islandCount = 0;
        for (int i = 0; i < oceanMap.grid.length; ++i) {
            for (int j = 0; j < oceanMap.grid[i].length; ++j) {
                if (i > 0 && oceanMap.grid[i - 1][j]) { continue; }
                if (j > 0 && oceanMap.grid[i][j - 1]) { continue; }
                if (oceanMap.grid[i][j]) {
                    ++islandCount;
                }
            }
        }
        return islandCount;
    }

    public static void test() {
        boolean[][] testGrid = {{true, false, false}, {true, false, true},
            {false, true, false}};
        OceanGridMap oceanMap = new OceanGridMap(testGrid);
        System.out.println(OceanGridMap.countIslands(oceanMap));
    }

    public static void main(String args[]) {
        test();
    }
}
