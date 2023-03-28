package baekjoon.silver.level2;

import java.util.Scanner;

public class BOJ_1780 {
    static int[][] map;
    static int answer1;
    static int answer2;
    static int answer3;

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();

        map = new int[num][num];

        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                map[i][j] = scan.nextInt();
            }
        }

        dfs(0, 0, num);

        System.out.println(answer1);
        System.out.println(answer2);
        System.out.println(answer3);
    }

    static void dfs(int x, int y, int size) {

        if (isSame(x, y, size)) {
            if (map[x][y] == -1) {
                answer1++;
            } else if (map[x][y] == 0) {
                answer2++;
            } else {
                answer3++;
            }
            return;
        }

        int newSize = size / 3;

        dfs(x, y, newSize);
        dfs(x, y + newSize, newSize);
        dfs(x, y + newSize * 2, newSize);

        dfs(x + newSize, y, newSize);
        dfs(x + newSize, y + newSize, newSize);
        dfs(x + newSize, y + newSize * 2, newSize);

        dfs(x + newSize * 2, y, newSize);
        dfs(x + newSize * 2, y + newSize, newSize);
        dfs(x + newSize * 2, y + newSize * 2, newSize);
    }

    static boolean isSame(int x, int y, int size) {
        int num = map[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (num != map[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}
