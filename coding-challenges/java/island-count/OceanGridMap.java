import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;

class OceanGridMap {
    private static Integer[] UP = {-1, 0};
    private static Integer[] LEFT = {0, -1};
    private static Integer[] RIGHT = {0, 1};
    private static Integer[] DOWN = {1, 0};

    public boolean[][] grid;

    public OceanGridMap(boolean[][] grid) {
        this.grid = grid;
    }

    private int countNumberOfIslands() {
        int islandCount = 0;
        for (int i = 0; i < this.grid.length; ++i) {
            for (int j = 0; j < this.grid[i].length; ++j) {
                if (this.grid[i][j]) {
                    ++islandCount;
                    this.deleteIslandDfs(new Integer[]{i, j});
                }
            }
        }

        return islandCount;
    }

    private void deleteIslandDfs(Integer[] coordinates) {
        ArrayDeque<Integer[]> stack;
        Integer[] landParcel;

        stack = new ArrayDeque<Integer[]>();
        stack.push(coordinates);

        while (!stack.isEmpty()) {
            landParcel = stack.pop();
            this.setCoord(landParcel, false);

            for (Integer[] neighbor : this.getNeighborsIfLand(landParcel)) {
                stack.push(neighbor);
            }
        }
    }

    private boolean isLand(Integer[] coordinates) {
        return this.grid[coordinates[0]][coordinates[1]];
    }

    private void setCoord(Integer[] coordinates, boolean value) {
        this.grid[coordinates[0]][coordinates[1]] = value;
    }

    private ArrayList<Integer[]> getNeighborsIfLand(Integer[] coordinates) {
        ArrayList<Integer[]> neighbors;
        neighbors = new ArrayList<Integer[]>();

        if (coordinates[0] != this.grid.length - 1) {
            Integer[] below = addCoords(coordinates, DOWN);
            if (this.isLand(below)) {
                neighbors.add(below);
            }
        }

        if (coordinates[1] != this.grid[coordinates[0]].length - 1) {
            Integer[] right = addCoords(coordinates, RIGHT);
            if (this.isLand(right)) {
                neighbors.add(right);
            }
        }

        if (coordinates[0] != 0) {
            Integer[] above = addCoords(coordinates, UP);
            if (this.isLand(above)) {
                neighbors.add(above);
            }
        }

        if (coordinates[1] != 0) {
            Integer[] left = addCoords(coordinates, LEFT);
            if (this.isLand(left)) {
                neighbors.add(left);
            }
        }

        return neighbors;
    }

    public static Integer[] addCoords(Integer[] coordinatesBefore, Integer[] coordinatesDelta) {
        return new Integer[] {coordinatesBefore[0] + coordinatesDelta[0],
                              coordinatesBefore[1] + coordinatesDelta[1]};
    }

    public static void test() {
        boolean[][] easyGrid = {
                {true, false, false},
                {true, false, true},
                {false, true, false}
        };
        OceanGridMap.testGrid(easyGrid, "Easy Grid", 3);

        boolean[][] grid1 = {
                {true, false, false, false},
                {true, true, false, false},
                {false, false, true, false},
                {false, true, true, false},
                {true, true, false, false},
                {false, false, true, false}
        };
        OceanGridMap.testGrid(grid1, "Grid 1", 3);
    }

    public void printPrettyGrid() {
        System.out.println("Showing state of grid...");
        for (boolean[] row : this.grid) {
            System.out.println(Arrays.toString(row));
        }
    }

    public static void testGrid(boolean[][] grid, String name, int correctCount) {
        OceanGridMap oceanMap = new OceanGridMap(grid);
        System.out.println("Correct Count is: " + correctCount);
        int dfsCount = oceanMap.countNumberOfIslands();
        System.out.println(dfsCount + " -- " + ((dfsCount == correctCount) ? "CORRECT" : "WRONG"));
        oceanMap.printPrettyGrid();
    }

    public static void main(String args[]) {
        test();
    }
}
