package com.products;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Основное приложение с консольным интерфейсом
 */
public class ProductApp {
    private static List<Product> products = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean running = true;

        while (running) {
            printMenu();
            int choice = getIntInput("Выберите пункт меню: ");

            switch (choice) {
                case 1:
                    addProduct();
                    break;
                case 2:
                    deleteProduct();
                    break;
                case 3:
                    displayAllProducts();
                    break;
                case 4:
                    compareProducts();
                    break;
                case 5:
                    running = false;
                    System.out.println("Приложение завершено.");
                    break;
                default:
                    System.out.println("Неверный выбор. Попробуйте снова.");
            }
        }
        scanner.close();
    }

    private static void printMenu() {
        System.out.println("\n=== Меню приложения ===");
        System.out.println("1. Добавить новый элемент");
        System.out.println("2. Удалить элемент по индексу");
        System.out.println("3. Вывод всех элементов");
        System.out.println("4. Сравнение двух элементов на равенство");
        System.out.println("5. Завершение работы");
        System.out.print("> ");
    }

    private static void addProduct() {
        System.out.println("\nВыберите тип продукта:");
        System.out.println("1. Фрукт");
        System.out.println("2. Молочная продукция");
        System.out.println("3. Мясо");
        
        int typeChoice = getIntInput("Введите номер типа: ");
        
        String name = getStringInput("Введите название: ");
        double price = getDoubleInput("Введите цену (0-1000000): ", 0, 1000000);

        Product product = null;

        switch (typeChoice) {
            case 1: // Фрукт
                String origin = getStringInput("Введите страну происхождения: ");
                double weight = getDoubleInput("Введите вес в кг (0-100): ", 0, 100);
                product = new Fruit(name, price, origin, weight);
                break;
            case 2: // Молочная продукция
                int fatContent = getIntInput("Введите процент жирности (0-100): ", 0, 100);
                String expirationDate = getStringInput("Введите срок годности: ");
                product = new DairyProduct(name, price, fatContent, expirationDate);
                break;
            case 3: // Мясо
                String meatType = getStringInput("Введите вид мяса: ");
                double meatWeight = getDoubleInput("Введите вес в кг (0-100): ", 0, 100);
                product = new Meat(name, price, meatType, meatWeight);
                break;
            default:
                System.out.println("Неверный тип продукта.");
                return;
        }

        products.add(product);
        System.out.println("Продукт успешно добавлен!");
    }

    private static void deleteProduct() {
        if (products.isEmpty()) {
            System.out.println("Список продуктов пуст.");
            return;
        }

        displayAllProducts();
        int index = getIntInput("Введите индекс элемента для удаления: ", 0, products.size() - 1);

        if (index >= 0 && index < products.size()) {
            Product removed = products.remove(index);
            System.out.println("Элемент удален: " + removed);
        } else {
            System.out.println("Неверный индекс.");
        }
    }

    private static void displayAllProducts() {
        if (products.isEmpty()) {
            System.out.println("Список продуктов пуст.");
            return;
        }

        System.out.println("\n=== Список продуктов ===");
        for (int i = 0; i < products.size(); i++) {
            System.out.println(i + ": " + products.get(i));
        }
    }

    private static void compareProducts() {
        if (products.size() < 2) {
            System.out.println("Недостаточно элементов для сравнения (минимум 2).");
            return;
        }

        displayAllProducts();
        int index1 = getIntInput("Введите индекс первого элемента: ", 0, products.size() - 1);
        int index2 = getIntInput("Введите индекс второго элемента: ", 0, products.size() - 1);

        if (index1 >= 0 && index1 < products.size() && 
            index2 >= 0 && index2 < products.size()) {
            
            Product p1 = products.get(index1);
            Product p2 = products.get(index2);

            System.out.println("\nЭлемент 1: " + p1);
            System.out.println("Элемент 2: " + p2);
            System.out.println("Равны: " + p1.equals(p2));
        } else {
            System.out.println("Неверные индексы.");
        }
    }

    // Методы для ввода с проверкой
    private static int getIntInput(String prompt) {
        while (true) {
            System.out.print(prompt);
            try {
                return Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("Ошибка: введите целое число.");
            }
        }
    }

    private static int getIntInput(String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            try {
                int value = Integer.parseInt(scanner.nextLine().trim());
                if (value >= min && value <= max) {
                    return value;
                } else {
                    System.out.println("Ошибка: число должно быть в диапазоне от " + min + " до " + max);
                }
            } catch (NumberFormatException e) {
                System.out.println("Ошибка: введите целое число.");
            }
        }
    }

    private static double getDoubleInput(String prompt, double min, double max) {
        while (true) {
            System.out.print(prompt);
            try {
                double value = Double.parseDouble(scanner.nextLine().trim());
                if (value >= min && value <= max) {
                    return value;
                } else {
                    System.out.println("Ошибка: число должно быть в диапазоне от " + min + " до " + max);
                }
            } catch (NumberFormatException e) {
                System.out.println("Ошибка: введите число.");
            }
        }
    }

    private static String getStringInput(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine().trim();
    }
}
