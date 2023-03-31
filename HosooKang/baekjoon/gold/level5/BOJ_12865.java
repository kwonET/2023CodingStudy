package baekjoon.gold.level5;

import java.util.Scanner;

public class BOJ_12865 {
    static int[] dy;

    static int solution(int[][] arr, int max) {
        dy = new int[max + 1];

        for (int i = 0; i < arr.length; i++) {
            for (int j = max; j >= arr[i][0]; j--) {
                dy[j] = Math.max(dy[j], dy[j - arr[i][0]] + arr[i][1]);
            }
        }

        return dy[max];
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int a = scan.nextInt();
        int b = scan.nextInt();

        int[][] arr = new int[a][2];
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < 2; j++) {
                arr[i][j] = scan.nextInt();
            }
        }

        int solution = solution(arr, b);

        System.out.println(solution);
    }
}
