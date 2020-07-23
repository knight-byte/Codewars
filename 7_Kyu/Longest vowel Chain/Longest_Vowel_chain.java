import java.util.Arrays;

class Solution {
    public static int solve(String s) {
        return Arrays.stream(s.split("[^aeiou]")).mapToInt(i -> i.length()).max().getAsInt();
    }
}