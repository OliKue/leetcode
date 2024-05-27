class Solution {
    public int romanToInt(String s) {
        HashMap<Character, Integer> values = new HashMap();
        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);

        // Initialize result
        int res = 0;

        for (int i = 0; i < s.length(); i++) {

            int s1 = values.get(s.charAt(i));

            if (i + 1 < s.length()) {
                int s2 = values.get(s.charAt(i + 1));

                if (s1 >= s2) {
                    res = res + s1;
                } else {

                    res = res + s2 - s1;
                    i++;
                }
            } else {
                res = res + s1;
            }
        }

        return res;
    }
}