class Kata {

    public static long find_ways(double m, double n) {
        if (n == 0)
            return 0;
        else
            m = m + n - 1;
        n = n - 1;
        double c = 1;
        double b = 1;
        for (double i = 0; i < n; i++) {
            c = c * (m - i);
            b = b * (i + 1);
        }
        return (long) (c / b);
    }
}