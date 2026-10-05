class Solution {
    public int daysBetweenDates(String date1, String date2) {
        java.time.LocalDate d1 = java.time.LocalDate.parse(date1);
        java.time.LocalDate d2 = java.time.LocalDate.parse(date2);

        return Math.abs((int) java.time.temporal.ChronoUnit.DAYS.between(d1, d2));
    }
}
