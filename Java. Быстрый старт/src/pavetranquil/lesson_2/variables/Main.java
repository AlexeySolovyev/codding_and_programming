package pavetranquil.lesson_2.variables;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введите операцию:");
        System.out.println("1. Сложение");
        System.out.println("2. Вычитание");
        System.out.println("3. Умножение");
        System.out.println("4. Деление");

        int operation = scanner.nextInt();

        System.out.println("Введите числа:");
        float a = scanner.nextInt();
        float b = scanner.nextInt();

        float result = 0;
        if (operation == 1){
            result = a + b;
        } else if (operation == 2) {
            result = a - b;
        } else if (operation == 3) {
            result = a * b;
        } else if (operation == 4) {
            result = a / b;
        }
        System.out.println("Ответ: " + result);

        scanner.close();

    }
}
