public class CountingDuplicates {
    public static int duplicateCount(String text) {
        int ans = 0;
        text = text.toLowerCase();
        while (text.length() > 0) {
            String firstLetter = text.substring(0, 1);
            text = text.substring(1);
            if (text.contains(firstLetter))
                ans++;
            text = text.replace(firstLetter, "");
        }
        return ans;
    }
}