        int count = 0;
        int sum = 0;

        for (int i = 0; i < m; i++) {
            sum += s.get(i);
        }

        if (sum == d) {
            count++;
        }

        for (int i = m; i < s.size(); i++) {
            sum += s.get(i);
            sum -= s.get(i - m);

            if (sum == d) {
                count++;
            }
        }

        return count;
