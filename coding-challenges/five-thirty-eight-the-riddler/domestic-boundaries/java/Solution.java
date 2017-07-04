/**
 * Created by jmq on 3/22/17.
 */
public class Solution {

    private static int NUM_SIMULATIONS = 100;

    public static void main(String[] args) {
        int convexCount = 0;

        for (int i = 0; i < NUM_SIMULATIONS; ++i) {
            RanchGrid ranchGrid = new RanchGrid();
            if (ranchGrid.isConvex()) {
                convexCount++;
            }
        }

        double estimatedProbability = (NUM_SIMULATIONS - convexCount) / NUM_SIMULATIONS;
        System.out.println("Finished. Estimated probability: " + estimatedProbability);
    }
}
