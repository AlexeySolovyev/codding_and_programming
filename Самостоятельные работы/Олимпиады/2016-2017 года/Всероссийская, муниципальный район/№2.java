package pavetranquil.test;

import java.util.Arrays;
import java.util.Scanner;


public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int p = in.nextInt();
        int q = in.nextInt();
        int[][] res = new int[10000][2];
        int m = 0;
        for (int b = 2; b <= n; b++) {
            for (int a = 1; a < b; a++) {
                boolean ok = true;
                for (int d = 2; d <= a; d++) {
                    if (a % d == 0 && b % d == 0) ok = false;
                }
                if (ok && a * p > b && a * q < b) {
                    res[m][0] = a;
                    res[m][1] = b;
                    m++;
                }
            }
        }
        Arrays.sort(res, 0, m, (o1, o2) -> Integer.compare(o1[0] * o2[1], o2[0] * o1[1]));
        for (int i = 0; i < m; i++) {
            System.out.println(res[i][0] + "/" + res[i][1]);
        }
    }
}
