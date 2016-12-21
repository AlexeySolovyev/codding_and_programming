package pavetranquil.lesson_3.cycle_while_and_start_game;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int range = 100;
        int answer = (int)(Math.random() * range);

        System.out.println("Угадайте число от 0 до " + range + "!");

        while (true){
            int input = scanner.nextInt();
            if (input > answer) {
                System.out.println("Ваше число больше загаданного!");
            } else if (input < answer) {
                System.out.println("Ваше число меньше загаданного!");
            } else if (input == answer) {
                System.out.println("Вы угадали число!");
                break;
            } else {
                System.out.println("ERROR!");
            }

        }
        scanner.close();
    }
}
