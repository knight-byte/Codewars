public class SystemOfEq {
    public static int Solution(int n, int m) {
        int count = 0;
        for (int a = 0, b; a <= Math.sqrt(n); a++)
            if ((b = n - a * a) * b + a == m)
                count++;
        return count;
    }
}