import java.util.*;

public class Prime {
    public static boolean isPrime(int num) {

        if (num <= 0 || num == 1) {
            return false;
        }
        int a = (int) Math.sqrt(num);

        for (int i = 2; i <= a; i++) {

            if (num % i == 0) {

                return false;

            }
        }

        return true;
    }
}