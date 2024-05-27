class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {

        // sort products
        ArrayList<String> sortedProducts = new ArrayList<>(Arrays.asList(products));
        Collections.sort(sortedProducts);

        // find matches
        List<List<String>> retList = new LinkedList();
        String temp= "";
        for(char c: searchWord.toCharArray()){
            temp = temp + c;

            List<String> matchList = new ArrayList();
            int i = 0;
            while(matchList.size() < 3 && i < sortedProducts.size()) {
                if(sortedProducts.get(i).startsWith(temp)){
                    matchList.add(sortedProducts.get(i));
                }
                i++;
            }
            retList.add(matchList);
        }
        return retList;
    }
}