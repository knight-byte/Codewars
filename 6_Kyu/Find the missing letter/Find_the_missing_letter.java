public class Kata {
    public static char findMissingLetter(char[] array) {
        char expectableLetter = array[0];
        for (char letter : array) {
            if (letter != expectableLetter)
                break;
            expectableLetter++;
        }
        return expectableLetter;
    }
}