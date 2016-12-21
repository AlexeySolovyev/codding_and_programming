package pavetranquil.lesson_4.methods_and_game;

import java.util.Scanner;

public class Main {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int range = 100;
        int answer = (int)(Math.random() * range);

        System.out.println("Угадайте число от 0 до " + range + "!");
        playGame(answer);

        scanner.close();
    }

    private static void playGame(int answer) {
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
    }
}
