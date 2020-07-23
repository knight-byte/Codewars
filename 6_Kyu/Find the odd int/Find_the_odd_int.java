public class FindOdd {
    public static int findIt(int[] a) {
        int odd = 0;
        for (int q : a)
            odd ^= q;
        return odd;
    }
}