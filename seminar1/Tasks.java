import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Tasks {
    /**
     * Подсчет суммы четных чисел от 1 до N. Напишите программу,
     * используя цикл, которая находит сумму всех четных чисел в диапазоне от 1 до заданного числа N.
     *
     * @param n N
     * @return сумма четных чисел
     */
    public static int evenSum(int n) {
        int sum = 0;
        for (int i = 1; i <= n / 2; i++) {
            sum += i * 2;
        }
        return sum;
    }

    /**
     * Поиск наименьшего числа в списке.
     * Напишите программу, которая находит наименьшее число в заданном списке с помощью цикла.
     *
     * @param array список чисел
     * @return наименьшее число
     */
    public static int minValue(Integer[] array) {
        int minValue = array[0];
        for (int value : array) {
            if (value < minValue) minValue = value;
        }

        return minValue;
    }

    /**
     * Вычисление факториала числа. Напишите программу,
     * которая находит факториал заданного числа N с использованием рекурсии или встроенных функций.
     *
     * @param n N
     * @return N!
     */
    public static long fact(int n) {
        return n == 1 ? 1 : n * fact(n - 1);
    }

    /**
     * Поиск уникальных элементов в списке.
     * Напишите программу, которая создает новый список,
     * содержащий только уникальные элементы из исходного списка.
     *
     * @param array исходный список
     * @return список с уникальными элементами
     */
    public static HashSet<Integer> uniqueNumbers(Integer[] array) {

        return new HashSet<Integer>(Arrays.asList(array));
    }

    /**
     * Вычисление суммы цифр числа. Напишите программу,
     * которая вычисляет сумму всех цифр заданного числа,
     * используя математические операции и деление нацело.
     *
     * @param num число
     * @return сумма цифр числа
     */

    public static int numSum(int num) {
        return num == 0 ? 0 : num % 10 + numSum(num / 10);
    }


    public static void main(String[] args) {

        System.out.println(evenSum(4)); // Задание 1

        Integer[] testArray = {1, 2, 3, 4, 5, 4, 3, 2, 1};

        System.out.println(minValue(testArray)); // задание 2

        System.out.println(fact(4)); // задание 3

        System.out.println(uniqueNumbers(testArray)); // Задание 4

        System.out.println(numSum(1024)); // Задание 8


    }

}
