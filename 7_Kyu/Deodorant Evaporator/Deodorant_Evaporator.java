public class Evaporator {

    public static int evaporator(double content, double evap_per_day, double threshold) {

        int nbOfDays = 0;
        double contentPercentage = 100;

        while (contentPercentage > threshold) {
            contentPercentage *= 1 - evap_per_day / 100;
            nbOfDays++;
        }

        return nbOfDays;
    }
}