/*
 * Refreshing my Java syntax.
 * To make sure that it works correctly, after compiling with javac,
 * run file with assertions enabled (for testing functionality).
 *
 * e.g. 
 * javac Euclid.java
 * java -ea Euclid
 */
class Euclid {
    public static int greatestCommonDivisor(int a, int b) {
        if (b == 0 || a == 0) { return a; }
        return greatestCommonDivisor(b, a % b);
    }

    public static void main(String args[]) {
        test();
    }

    public static void test() {
        int[][] testCases = {{20, 4}, {100, 10}, {30, 12}, {0, 0}, {0, 1}};
        int[] answers = {4, 10, 6, 0, 0};
        System.out.println("Beginning tests...");
        for (int i = 0; i < testCases.length; ++i) {
            int a = testCases[i][0];
            int b = testCases[i][1];
            int result = greatestCommonDivisor(a, b);
            assert result == answers[i];
            System.out.println("(" + a + ", " + b + ") -> " + result);
        }
    }
}
