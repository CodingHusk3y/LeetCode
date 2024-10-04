import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
        {
            return false;
        }

        char[] list_s = s.toCharArray();
        char[] list_t = t.toCharArray();

        Arrays.sort(list_s);
        Arrays.sort(list_t);

        return Arrays.equals(list_s, list_t);
    }
}