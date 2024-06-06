class Solution {

    public String intToRoman(int num) {
        int thousend = num/1000;
        int hundred = (num - (thousend*1000)) / 100 ;
        int tens = (num -(thousend*1000) - (hundred*100)) / 10;
        int ones = (num - (thousend*1000) - (hundred*100) - (tens * 10));

        String result = "";

        HashMap thTa = new HashMap<Integer, String>();
        thTa.put(1, "M");
        thTa.put(2, "MM");
        thTa.put(3, "MMM");

        result = result + thTa.getOrDefault(thousend,"");

        HashMap huTa = new HashMap<Integer, String>();
        huTa.put(1, "C");
        huTa.put(2, "CC");
        huTa.put(3, "CCC");
        huTa.put(4, "CD");
        huTa.put(5, "D");
        huTa.put(6, "DC");
        huTa.put(7, "DCC");
        huTa.put(8, "DCCC");
        huTa.put(9, "CM");

        result = result + huTa.getOrDefault(hundred,"");

        HashMap teTa = new HashMap<Integer, String>();
        teTa.put(1, "X");
        teTa.put(2, "XX");
        teTa.put(3, "XXX");
        teTa.put(4, "XL");
        teTa.put(5, "L");
        teTa.put(6, "LX");
        teTa.put(7, "LXX");
        teTa.put(8, "LXXX");
        teTa.put(9, "XC");

        result = result + teTa.getOrDefault(tens,"");

        HashMap onTa = new HashMap<Integer, String>();
        onTa.put(1, "I");
        onTa.put(2, "II");
        onTa.put(3, "III");
        onTa.put(4, "IV");
        onTa.put(5, "V");
        onTa.put(6, "VI");
        onTa.put(7, "VII");
        onTa.put(8, "VIII");
        onTa.put(9, "IX");

        result = result + onTa.getOrDefault(ones,"");

        return result;
    }
}