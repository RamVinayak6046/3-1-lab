class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();

        if (s.length() < p.length()) {
            return result;
        }

        int[] count = new int[26];

        for (char c : p.toCharArray()) {
            count[c - 'a']++;
        }

        int left = 0;
        int right = 0;
        int required = p.length();

        while (right < s.length()) {
            char c = s.charAt(right);

            if (count[c - 'a'] > 0) {
                required--;
            }

            count[c - 'a']--;
            right++;

            if (right - left == p.length()) {
                if (required == 0) {
                    result.add(left);
                }

                char leftChar = s.charAt(left);

                if (count[leftChar - 'a'] >= 0) {
                    required++;
                }

                count[leftChar - 'a']++;
                left++;
            }
        }

        return result;
    }
}
