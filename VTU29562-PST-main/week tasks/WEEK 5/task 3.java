        int maxSubarraySum = arr.get(0);
        int currentSum = arr.get(0);

        int maxSubsequenceSum = arr.get(0);

        for (int i = 1; i < arr.size(); i++) {

            currentSum = Math.max(arr.get(i), currentSum + arr.get(i));

            maxSubarraySum = Math.max(maxSubarraySum, currentSum);

            maxSubsequenceSum =
                Math.max(maxSubsequenceSum,
                         Math.max(arr.get(i), maxSubsequenceSum + arr.get(i)));
        }

        List<Integer> result = new ArrayList<>();

        result.add(maxSubarraySum);
        result.add(maxSubsequenceSum);

        return result;
