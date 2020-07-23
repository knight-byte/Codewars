public class Solution {

    public static int signChange(int[] arr) {
        int count = 0;
        for (int i = 1; i < arr.length; i++) {
            if ((arr[i] >= 0 && arr[i - 1] < 0) || (arr[i] < 0 && arr[i - 1] >= 0))
                count++;
        }
        return count;
    }

}