package com.products;

/**
 * Класс Фрукт - наследник Product
 */
public class Fruit extends Product {
    private String origin; // страна происхождения
    private double weight; // вес в кг

    // Конструктор по умолчанию
    public Fruit() {
        super();
        this.origin = "";
        this.weight = 0.0;
    }

    // Конструктор с параметрами
    public Fruit(String name, double price, String origin, double weight) {
        super(name, price);
        setOrigin(origin);
        setWeight(weight);
    }

    public String getOrigin() {
        return origin;
    }

    public void setOrigin(String origin) {
        if (origin != null && !origin.trim().isEmpty()) {
            this.origin = origin.trim();
        } else {
            this.origin = "Неизвестно";
        }
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        if (weight > 0 && weight <= 100) {
            this.weight = weight;
        } else {
            this.weight = 0.0;
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!super.equals(obj)) return false;
        if (getClass() != obj.getClass()) return false;
        Fruit fruit = (Fruit) obj;
        return Double.compare(fruit.weight, weight) == 0 &&
               origin.equals(fruit.origin);
    }

    @Override
    public int hashCode() {
        int result = super.hashCode();
        long temp;
        result = 31 * result + (origin != null ? origin.hashCode() : 0);
        temp = Double.doubleToLongBits(weight);
        result = 31 * result + (int) (temp ^ (temp >>> 32));
        return result;
    }

    @Override
    public String toString() {
        return "Fruit{name='" + name + "', price=" + price + 
               ", origin='" + origin + "', weight=" + weight + "}";
    }
}
