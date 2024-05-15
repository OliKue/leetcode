class Solution {

    public int[][] kClosest(int[][] points, int k) {
        List<int[]> listPoints = new LinkedList(points);

        for(int[] xy: points) {
            listPoints.add(xy);
        }

        Collections.sort(listPoints, new Comparator<int[]>() {
            @Override
            public int compare(int[] left, int[] right) {
                return getDistance(left) - getDistance(right);
            }});

        // return k first elements of sorted list
        int[][] retArr = new int[k][2];
        for(int i = 0; i < k; i++){
            retArr[i] = listPoints.get(i);
        }

        return retArr;
    }

    private int getDistance(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}
