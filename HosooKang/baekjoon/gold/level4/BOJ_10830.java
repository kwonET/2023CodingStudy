package baekjoon.gold.level4;

import java.util.Scanner;

public class BOJ_10830 {

    final static int MOD = 1000;
    public static int N;
    public static int[][] origin;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        N = scan.nextInt();
        long B = scan.nextLong();

        origin = new int[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                origin[i][j] = scan.nextInt() % MOD;
            }
        }

        int[][] result = pow(origin, B);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(result[i][j]).append(' ');
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    public static int[][] pow(int[][] A, long exp) {
        if (exp == 1L) {
            return A;
        }

        int[][] arr = pow(A, exp / 2);
        arr = mul(arr, arr);

        if (exp % 2 == 1L) {
            arr = mul(arr, origin);
        }

        return arr;
    }

    public static int[][] mul(int[][] arr1, int[][] arr2) {
        int[][] arr3 = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    arr3[i][j] += arr1[i][k] * arr2[k][j];
                    arr3[i][j] %= MOD;
                }
            }
        }
        return arr3;
    }
}

