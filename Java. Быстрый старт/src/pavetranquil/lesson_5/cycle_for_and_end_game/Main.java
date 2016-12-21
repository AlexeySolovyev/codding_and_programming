package pavetranquil.lesson_5.cycle_for_and_end_game;

import java.util.Scanner;

public class Main {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
//        for (int i = 1; i <= 10; i += 1) {
//            System.out.println(i);
//        }

        System.out.println("Добро пожаловать в игру Угадай число!");
        System.out.println("Вам предстоит пройти 3 уровня!");

        for (int range = 20; range <= 100; range += 40) playGame(range);

        System.out.println("Поздравляю! Вы выиграли!");
        System.out.println("Спасибо за игру! До свидания!");

        scanner.close();
    }

    private static void playGame(int range) {
        System.out.println("Угадайте число от 0 до " + range + "!");
        int answer = (int) (Math.random() * range);
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
