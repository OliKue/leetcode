class Solution {
    LinkedList<String> digitLogs = new LinkedList();
    HashMap<String, String> letterLogs = new HashMap();

    public String[] reorderLogFiles(String[] logs) {
        // Seperate logs
        for (String log : logs) {
            int firstLogCharIndex = log.indexOf(' ') + 1;
            if (Character.isDigit(log.charAt(firstLogCharIndex))) {
                digitLogs.add(log);
            } else {
                letterLogs.put(log, log.substring(firstLogCharIndex));
            }
        }

        // Sort letter logs
        List<Map.Entry<String, String>> entries = new ArrayList<Map.Entry<String, String>>(letterLogs.entrySet());

        Collections.sort(entries, (Map.Entry<String, String> val1, Map.Entry<String, String> val2) -> {
            if (val1.getValue().equals(val2.getValue())) {
                return val1.getKey().compareTo(val2.getKey());
            } else {
                return val1.getValue().compareTo(val2.getValue());
            }
        });

        // Merge lists
        String[] retArr = new String[logs.length];

        for(int i = 0; i < logs.length; i++) {
            if(i < entries.size()){
                retArr[i] = entries.get(i).getKey();
            }else{
                retArr[i] = digitLogs.get(i - entries.size());
            }

        }
        return retArr;
    }

}
