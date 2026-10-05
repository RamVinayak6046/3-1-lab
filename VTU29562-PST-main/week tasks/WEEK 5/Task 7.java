class Solution {
    public int lengthOfLongestSubstring(String s) {

        int left = 0;
        int maxLength = 0;

        int[] lastIndex = new int[128];

        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);

            left = Math.max(left, lastIndex[ch]);

            maxLength = Math.max(maxLength, right - left + 1);

            lastIndex[ch] = right + 1;
        }

        return maxLength;
    }
}
