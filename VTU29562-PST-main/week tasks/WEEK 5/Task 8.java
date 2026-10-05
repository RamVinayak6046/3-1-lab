class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> result = new ArrayList<>();
        for (String word : words) {
            if (matches(word, pattern)) {
                result.add(word);
            }
        }
        return result;
    }

    private boolean matches(String word, String pattern) {
        if (word.length() != pattern.length()) {
            return false;
        }
        int[] wordToPattern = new int[26];
        int[] patternToWord = new int[26];
        Arrays.fill(wordToPattern, -1);
        Arrays.fill(patternToWord, -1);
        for (int i = 0; i < word.length(); i++) {
            int w = word.charAt(i) - 'a';
            int p = pattern.charAt(i) - 'a';

            if (wordToPattern[w] == -1 &&
                patternToWord[p] == -1) {
                wordToPattern[w] = p;
                patternToWord[p] = w;
            } else if (wordToPattern[w] != p ||
                       patternToWord[p] != w) {
                return false;
            }
        }
        return true;
    }
}
