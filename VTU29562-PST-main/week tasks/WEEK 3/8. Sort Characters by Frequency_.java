class Solution {
    public String frequencySort(String s) {
        HashMap<Character, Integer> map = new HashMap<>();

        for (char c : s.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0) + 1);
        }

        List<Character> list = new ArrayList<>(map.keySet());

        Collections.sort(list, new Comparator<Character>() {
            public int compare(Character a, Character b) {
                return map.get(b) - map.get(a);
            }
        });

        StringBuilder result = new StringBuilder();

        for (char c : list) {
            for (int i = 0; i < map.get(c); i++) {
                result.append(c);
            }
        }

        return result.toString();
    }
}
