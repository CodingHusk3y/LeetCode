import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer, Integer> dictionary = new HashMap<>();

        for (int i : nums)
        {
            if (dictionary.containsKey(i))
            {
                return true;
            }
            else
            {
                dictionary.put(i, 1);
            }
        }

        return false;
    }
}