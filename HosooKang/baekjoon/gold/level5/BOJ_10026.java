package baekjoon.gold.level5;

import java.util.Scanner;

public class BOJ_10026 {
    static int[] dx = {-1, 0, 0, 1};
    static int[] dy = {0, 1, -1, 0};
    static char color[][];
    static boolean visit[][];
    static  int num;


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        num = scan.nextInt();

        color = new char[num + 1][num + 1];
        visit = new boolean[num + 1][num + 1];

        for (int i = 0; i < num; i++) {
            String str = scan.next();
            for (int j = 0; j<num; j++) {
                color[i][j] = str.charAt(j);
            }
        }

        int answer1 = 0;
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                if (!visit[i][j]) {
                    dfs(i, j);
                    answer1++;
                }
            }
        }

        visit = new boolean[num + 1][num + 1];
        int answer2 = 0;
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                if (color[i][j] == 'G') {
                    color[i][j] = 'R';
                }
            }
        }

        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                if (!visit[i][j]) {
                    dfs(i, j);
                    answer2++;
                }
            }
        }

        System.out.println(answer1 + " " + answer2);
    }

    static void dfs(int x, int y) {
        visit[x][y] = true;
        char tmp = color[x][y];
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx > num || ny > num) {
                continue;
            }

            if (!visit[nx][ny] && color[nx][ny] == tmp) {
                dfs(nx, ny);
            }
        }
    }
}
