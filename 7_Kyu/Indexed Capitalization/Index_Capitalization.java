package kata;

public class Solution {
    public static String capitalize(String s, int[] ind) {
        char[] array = s.toCharArray();
        for (int i = 0; i < ind.length; i++) {
            if (ind[i] < s.length()) {
                array[ind[i]] = Character.toUpperCase(array[ind[i]]);
            }
        }
        return String.valueOf(array);
    }
}