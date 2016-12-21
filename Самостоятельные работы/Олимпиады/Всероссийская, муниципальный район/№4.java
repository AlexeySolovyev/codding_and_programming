package pavetranquil.test;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] p = new int[n];
        for (int i = 0; i < n; i++) p[i] = i + 1;
        int res = 0;
        while (true) {
            int s = 0;
            for (int i = 0; i < n - 1; i++)
                s += p[i] * p[i + 1];
            if (s % k == 0)
                res++;
            int i = n - 2;
            while (i >= 0 && p[i] > p[i + 1]) i--;
            if (i < 0) break;
            int j = n - 1;
            while (p[j] < p[i]) j--;
            int t = p[i]; p[i] = p[j]; p[j] = t;
            Arrays.sort(p, i + 1, n);
        }
        System.out.println(res);
    }
}
