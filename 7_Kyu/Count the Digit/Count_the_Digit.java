public class CountDig {

    public static int nbDig(int n, int d) {
        int sum = 0;
        for (int i = 0; i <= n; i++) {
            sum += countOfDigit((int) Math.pow(i, 2), d);
        }
        return sum;
    }

    public static int countOfDigit(int n, int d) {
        int count = 0;
        do {
            if (n % 10 == d)
                count++;
            n /= 10;
        } while (n > 0);
        return count;
    }
}