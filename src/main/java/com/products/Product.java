package com.products;

/**
 * Базовый класс для всех продуктов
 */
public class Product {
    protected String name;
    protected double price;

    // Конструктор по умолчанию
    public Product() {
        this.name = "";
        this.price = 0.0;
    }

    // Конструктор с параметрами
    public Product(String name, double price) {
        setName(name);
        setPrice(price);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name.trim();
        } else {
            this.name = "Без названия";
        }
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if (price >= 0 && price <= 1000000) {
            this.price = price;
        } else {
            this.price = 0.0;
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Product product = (Product) obj;
        return Double.compare(product.price, price) == 0 &&
               name.equals(product.name);
    }

    @Override
    public int hashCode() {
        int result;
        long temp;
        result = name != null ? name.hashCode() : 0;
        temp = Double.doubleToLongBits(price);
        result = 31 * result + (int) (temp ^ (temp >>> 32));
        return result;
    }

    @Override
    public String toString() {
        return "Product{name='" + name + "', price=" + price + "}";
    }
}
