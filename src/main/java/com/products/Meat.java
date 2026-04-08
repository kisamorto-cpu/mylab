package com.products;

/**
 * Класс Мясо - наследник Product
 */
public class Meat extends Product {
    private String type; // вид мяса (говядина, свинина и т.д.)
    private double weight; // вес в кг

    // Конструктор по умолчанию
    public Meat() {
        super();
        this.type = "";
        this.weight = 0.0;
    }

    // Конструктор с параметрами
    public Meat(String name, double price, String type, double weight) {
        super(name, price);
        setType(type);
        setWeight(weight);
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        if (type != null && !type.trim().isEmpty()) {
            this.type = type.trim();
        } else {
            this.type = "Не указан";
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
        Meat meat = (Meat) obj;
        return Double.compare(meat.weight, weight) == 0 &&
               type.equals(meat.type);
    }

    @Override
    public int hashCode() {
        int result = super.hashCode();
        long temp;
        result = 31 * result + (type != null ? type.hashCode() : 0);
        temp = Double.doubleToLongBits(weight);
        result = 31 * result + (int) (temp ^ (temp >>> 32));
        return result;
    }

    @Override
    public String toString() {
        return "Meat{name='" + name + "', price=" + price + 
               ", type='" + type + "', weight=" + weight + "}";
    }
}
