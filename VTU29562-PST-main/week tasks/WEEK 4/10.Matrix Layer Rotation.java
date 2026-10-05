import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;

import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'matrixRotation' function below.
     *
     * The function accepts following parameters:
     *  1. 2D_INTEGER_ARRAY matrix
     *  2. INTEGER r
     */

    public static void matrixRotation(List<List<Integer>> matrix, int r) {

        int m = matrix.size();
        int n = matrix.get(0).size();

        // Number of layers
        int layers = Math.min(m, n) / 2;

        // Process each layer
        for (int layer = 0; layer < layers; layer++) {

            int top = layer;
            int left = layer;
            int bottom = m - 1 - layer;
            int right = n - 1 - layer;

            List<Integer> elements = new ArrayList<>();

            // 1. Top row: left -> right
            for (int j = left; j <= right; j++) {
                elements.add(matrix.get(top).get(j));
            }

            // 2. Right column: top -> bottom
            for (int i = top + 1; i <= bottom; i++) {
                elements.add(matrix.get(i).get(right));
            }

            // 3. Bottom row: right -> left
            for (int j = right - 1; j >= left; j--) {
                elements.add(matrix.get(bottom).get(j));
            }

            // 4. Left column: bottom -> top
            for (int i = bottom - 1; i > top; i--) {
                elements.add(matrix.get(i).get(left));
            }

            // Reduce unnecessary rotations
            int shift = r % elements.size();

            List<Integer> rotated = new ArrayList<>();

            // Anticlockwise rotation
            for (int i = shift; i < elements.size(); i++) {
                rotated.add(elements.get(i));
            }

            for (int i = 0; i < shift; i++) {
                rotated.add(elements.get(i));
            }

            int index = 0;

            // Put values back into top row
            for (int j = left; j <= right; j++) {
                matrix.get(top).set(j, rotated.get(index++));
            }

            // Put values back into right column
            for (int i = top + 1; i <= bottom; i++) {
                matrix.get(i).set(right, rotated.get(index++));
            }

            // Put values back into bottom row
            for (int j = right - 1; j >= left; j--) {
                matrix.get(bottom).set(j, rotated.get(index++));
            }

            // Put values back into left column
            for (int i = bottom - 1; i > top; i--) {
                matrix.get(i).set(left, rotated.get(index++));
            }
        }

        // Print the final matrix
        for (List<Integer> row : matrix) {
            System.out.println(
                row.stream()
                   .map(String::valueOf)
                   .collect(joining(" "))
            );
        }
    }
}

public class Solution {

    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader =
            new BufferedReader(
                new InputStreamReader(System.in)
            );

        String[] firstMultipleInput =
            bufferedReader.readLine()
                .replaceAll("\\s+$", "")
                .split(" ");

        int m = Integer.parseInt(firstMultipleInput[0]);

        int n = Integer.parseInt(firstMultipleInput[1]);

        int r = Integer.parseInt(firstMultipleInput[2]);

        List<List<Integer>> matrix = new ArrayList<>();

        IntStream.range(0, m).forEach(i -> {
            try {
                matrix.add(
                    Stream.of(
                        bufferedReader.readLine()
                            .replaceAll("\\s+$", "")
                            .split(" ")
                    )
                    .map(Integer::parseInt)
                    .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        Result.matrixRotation(matrix, r);

        bufferedReader.close();
    }
}
