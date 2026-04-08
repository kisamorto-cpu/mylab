package com.products;

/**
 * Класс Молочная продукция - наследник Product
 */
public class DairyProduct extends Product {
    private int fatContent; // процент жирности
    private String expirationDate; // срок годности

    // Конструктор по умолчанию
    public DairyProduct() {
        super();
        this.fatContent = 0;
        this.expirationDate = "";
    }

    // Конструктор с параметрами
    public DairyProduct(String name, double price, int fatContent, String expirationDate) {
        super(name, price);
        setFatContent(fatContent);
        setExpirationDate(expirationDate);
    }

    public int getFatContent() {
        return fatContent;
    }

    public void setFatContent(int fatContent) {
        if (fatContent >= 0 && fatContent <= 100) {
            this.fatContent = fatContent;
        } else {
            this.fatContent = 0;
        }
    }

    public String getExpirationDate() {
        return expirationDate;
    }

    public void setExpirationDate(String expirationDate) {
        if (expirationDate != null && !expirationDate.trim().isEmpty()) {
            this.expirationDate = expirationDate.trim();
        } else {
            this.expirationDate = "Не указан";
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!super.equals(obj)) return false;
        if (getClass() != obj.getClass()) return false;
        DairyProduct that = (DairyProduct) obj;
        return fatContent == that.fatContent &&
               expirationDate.equals(that.expirationDate);
    }

    @Override
    public int hashCode() {
        int result = super.hashCode();
        result = 31 * result + fatContent;
        result = 31 * result + (expirationDate != null ? expirationDate.hashCode() : 0);
        return result;
    }

    @Override
    public String toString() {
        return "DairyProduct{name='" + name + "', price=" + price + 
               ", fatContent=" + fatContent + "%, expirationDate='" + expirationDate + "'}";
    }
}
