import java.math.BigDecimal;
import java.util.concurrent.ThreadLocalRandom;

public class RanchGrid {
    BigDecimal[][] grid = new BigDecimal[4][2];

    public RanchGrid() {
        this.populate();
    }

    private void populate() {
        for (int i = 0; i < this.grid.length; ++i) {
            this.grid[i] = RanchGrid.newHouseLocation();
        }
    }

    public static BigDecimal[] newHouseLocation() {

        return new BigDecimal[]{
                BigDecimal.valueOf(ThreadLocalRandom.current().nextDouble(0, 1)),
                BigDecimal.valueOf(ThreadLocalRandom.current().nextDouble(0, 1))
        };
    }

    public boolean isConvex() {
        
    }

    private boolean isRightTurn(BigDecimal a, BigDecimal b, BigDecimal c) {

    }
}
