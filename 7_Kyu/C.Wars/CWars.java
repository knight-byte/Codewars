import java.lang.*;

class CWars {

    public static String initials(String name) {
        String[] s = name.split(" ");
        String print = "";
        for (int i = 0; i < s.length - 1; i++) {
            print += Character.toUpperCase(s[i].charAt(0)) + ".";
        }
        int last = s.length - 1;

        print += Character.toUpperCase(s[last].charAt(0)) + s[last].substring(1, s[last].length());
        System.out.println(print);
        return print;
    }

}