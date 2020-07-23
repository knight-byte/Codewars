class Kata {
    static String toLeetSpeak(final String speak) {
        StringBuilder sb = new StringBuilder(speak.length());
        for (char c : speak.toCharArray()) {
            switch (c) {
                case 'A':
                    sb.append('@');
                    break;
                case 'B':
                    sb.append('8');
                    break;
                case 'C':
                    sb.append('(');
                    break;
                case 'E':
                    sb.append('3');
                    break;
                case 'G':
                    sb.append('6');
                    break;
                case 'H':
                    sb.append('#');
                    break;
                case 'I':
                    sb.append('!');
                    break;
                case 'L':
                    sb.append('1');
                    break;
                case 'O':
                    sb.append('0');
                    break;
                case 'S':
                    sb.append('$');
                    break;
                case 'T':
                    sb.append('7');
                    break;
                case 'Z':
                    sb.append('2');
                    break;
                default:
                    sb.append(c);
                    break;
            }
        }
        return sb.toString();
    }
}