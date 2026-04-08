"""
Программа для управления коллекцией продуктов.
Иерархия классов: Продукты (базовый) -> Фрукты, МолочнаяПродукция, Мясо
"""

from abc import ABC
from typing import List, Optional


class Product(ABC):
    """Базовый класс для всех продуктов."""
    
    def __init__(self, name: str = "", price: float = 0.0):
        self._name = name
        self._price = price
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        self._price = value
    
    def equals(self, other: 'Product') -> bool:
        """Сравнение двух объектов на равенство."""
        if other is None or not isinstance(other, Product):
            return False
        return self._name == other._name and abs(self._price - other._price) < 0.001
    
    def hash_code(self) -> int:
        """Вычисление хэш-кода объекта."""
        return hash((self._name, round(self._price, 2)))
    
    def to_string(self) -> str:
        """Строковое представление объекта."""
        return f"Product(name='{self._name}', price={self._price:.2f})"
    
    def get_type(self) -> str:
        """Возвращает тип продукта."""
        return "Продукт"
    
    @staticmethod
    def validate_price(value: float) -> tuple[bool, str]:
        """Валидация цены."""
        try:
            price = float(value)
            if price < 0:
                return False, "Цена не может быть отрицательной"
            return True, ""
        except (ValueError, TypeError):
            return False, "Цена должна быть числом"
    
    @staticmethod
    def validate_name(value: str) -> tuple[bool, str]:
        """Валидация названия."""
        if not isinstance(value, str):
            return False, "Название должно быть строкой"
        if len(value.strip()) == 0:
            return False, "Название не может быть пустым"
        return True, ""


class Fruit(Product):
    """Класс для фруктов."""
    
    def __init__(self, name: str = "", price: float = 0.0, origin: str = "", weight: float = 0.0):
        super().__init__(name, price)
        self._origin = origin
        self._weight = weight
    
    @property
    def origin(self) -> str:
        return self._origin
    
    @origin.setter
    def origin(self, value: str):
        self._origin = value
    
    @property
    def weight(self) -> float:
        return self._weight
    
    @weight.setter
    def weight(self, value: float):
        self._weight = value
    
    def equals(self, other: 'Fruit') -> bool:
        """Сравнение двух объектов на равенство."""
        if other is None or not isinstance(other, Fruit):
            return False
        return (super().equals(other) and 
                self._origin == other._origin and 
                abs(self._weight - other._weight) < 0.001)
    
    def hash_code(self) -> int:
        """Вычисление хэш-кода объекта."""
        return hash((super().hash_code(), self._origin, round(self._weight, 2)))
    
    def to_string(self) -> str:
        """Строковое представление объекта."""
        return f"Fruit(name='{self._name}', price={self._price:.2f}, origin='{self._origin}', weight={self._weight:.2f}г)"
    
    def get_type(self) -> str:
        """Возвращает тип продукта."""
        return "Фрукт"
    
    @staticmethod
    def validate_weight(value) -> tuple[bool, str]:
        """Валидация веса."""
        try:
            weight = float(value)
            if weight <= 0:
                return False, "Вес должен быть положительным числом"
            if weight > 10000:
                return False, "Вес не может превышать 10000г"
            return True, ""
        except (ValueError, TypeError):
            return False, "Вес должен быть числом"
    
    @staticmethod
    def validate_origin(value: str) -> tuple[bool, str]:
        """Валидация страны происхождения."""
        if not isinstance(value, str):
            return False, "Страна должна быть строкой"
        if len(value.strip()) == 0:
            return False, "Страна не может быть пустой"
        return True, ""


class DairyProduct(Product):
    """Класс для молочной продукции."""
    
    def __init__(self, name: str = "", price: float = 0.0, fat_content: float = 0.0, expiration_days: int = 0):
        super().__init__(name, price)
        self._fat_content = fat_content
        self._expiration_days = expiration_days
    
    @property
    def fat_content(self) -> float:
        return self._fat_content
    
    @fat_content.setter
    def fat_content(self, value: float):
        self._fat_content = value
    
    @property
    def expiration_days(self) -> int:
        return self._expiration_days
    
    @expiration_days.setter
    def expiration_days(self, value: int):
        self._expiration_days = value
    
    def equals(self, other: 'DairyProduct') -> bool:
        """Сравнение двух объектов на равенство."""
        if other is None or not isinstance(other, DairyProduct):
            return False
        return (super().equals(other) and 
                abs(self._fat_content - other._fat_content) < 0.001 and 
                self._expiration_days == other._expiration_days)
    
    def hash_code(self) -> int:
        """Вычисление хэш-кода объекта."""
        return hash((super().hash_code(), round(self._fat_content, 2), self._expiration_days))
    
    def to_string(self) -> str:
        """Строковое представление объекта."""
        return f"DairyProduct(name='{self._name}', price={self._price:.2f}, fat={self._fat_content:.1f}%, expiration={self._expiration_days} дней)"
    
    def get_type(self) -> str:
        """Возвращает тип продукта."""
        return "Молочная продукция"
    
    @staticmethod
    def validate_fat_content(value) -> tuple[bool, str]:
        """Валидация жирности."""
        try:
            fat = float(value)
            if fat < 0:
                return False, "Жирность не может быть отрицательной"
            if fat > 100:
                return False, "Жирность не может превышать 100%"
            return True, ""
        except (ValueError, TypeError):
            return False, "Жирность должна быть числом"
    
    @staticmethod
    def validate_expiration_days(value) -> tuple[bool, str]:
        """Валидация срока годности."""
        try:
            days = int(value)
            if days < 0:
                return False, "Срок годности не может быть отрицательным"
            if days > 3650:
                return False, "Срок годности не может превышать 10 лет (3650 дней)"
            return True, ""
        except (ValueError, TypeError):
            return False, "Срок годности должен быть целым числом"


class Meat(Product):
    """Класс для мясной продукции."""
    
    def __init__(self, name: str = "", price: float = 0.0, animal_type: str = "", protein: float = 0.0):
        super().__init__(name, price)
        self._animal_type = animal_type
        self._protein = protein
    
    @property
    def animal_type(self) -> str:
        return self._animal_type
    
    @animal_type.setter
    def animal_type(self, value: str):
        self._animal_type = value
    
    @property
    def protein(self) -> float:
        return self._protein
    
    @protein.setter
    def protein(self, value: float):
        self._protein = value
    
    def equals(self, other: 'Meat') -> bool:
        """Сравнение двух объектов на равенство."""
        if other is None or not isinstance(other, Meat):
            return False
        return (super().equals(other) and 
                self._animal_type == other._animal_type and 
                abs(self._protein - other._protein) < 0.001)
    
    def hash_code(self) -> int:
        """Вычисление хэш-кода объекта."""
        return hash((super().hash_code(), self._animal_type, round(self._protein, 2)))
    
    def to_string(self) -> str:
        """Строковое представление объекта."""
        return f"Meat(name='{self._name}', price={self._price:.2f}, animal='{self._animal_type}', protein={self._protein:.1f}г)"
    
    def get_type(self) -> str:
        """Возвращает тип продукта."""
        return "Мясо"
    
    @staticmethod
    def validate_animal_type(value: str) -> tuple[bool, str]:
        """Валидация типа животного."""
        if not isinstance(value, str):
            return False, "Тип животного должен быть строкой"
        if len(value.strip()) == 0:
            return False, "Тип животного не может быть пустым"
        return True, ""
    
    @staticmethod
    def validate_protein(value) -> tuple[bool, str]:
        """Валидация содержания белка."""
        try:
            protein = float(value)
            if protein < 0:
                return False, "Содержание белка не может быть отрицательным"
            if protein > 100:
                return False, "Содержание белка не может превышать 100г"
            return True, ""
        except (ValueError, TypeError):
            return False, "Содержание белка должно быть числом"


class ProductManager:
    """Класс для управления коллекцией продуктов."""
    
    def __init__(self):
        self._products: List[Product] = []
    
    def add_product(self, product: Product) -> None:
        """Добавить продукт в коллекцию."""
        self._products.append(product)
    
    def remove_by_index(self, index: int) -> bool:
        """Удалить продукт по индексу."""
        if 0 <= index < len(self._products):
            del self._products[index]
            return True
        return False
    
    def get_all_products(self) -> List[Product]:
        """Получить все продукты."""
        return self._products.copy()
    
    def compare_by_index(self, index1: int, index2: int) -> Optional[bool]:
        """Сравнить два продукта по индексам на равенство."""
        if 0 <= index1 < len(self._products) and 0 <= index2 < len(self._products):
            return self._products[index1].equals(self._products[index2])
        return None
    
    def get_product_by_index(self, index: int) -> Optional[Product]:
        """Получить продукт по индексу."""
        if 0 <= index < len(self._products):
            return self._products[index]
        return None
    
    def size(self) -> int:
        """Вернуть количество продуктов."""
        return len(self._products)


def input_number(prompt: str, min_val: float = float('-inf'), max_val: float = float('inf'), is_int: bool = False) -> Optional[float]:
    """Ввод числа с проверкой диапазона."""
    while True:
        value = input(prompt)
        try:
            if is_int:
                num = int(value)
            else:
                num = float(value)
            
            if num < min_val or num > max_val:
                print(f"Число должно быть в диапазоне от {min_val} до {max_val}")
                continue
            return num
        except ValueError:
            print("Ошибка: введите корректное число")


def input_string(prompt: str, allow_empty: bool = False) -> str:
    """Ввод строки с проверкой."""
    while True:
        value = input(prompt)
        if allow_empty or len(value.strip()) > 0:
            return value
        print("Ошибка: строка не может быть пустой")


def add_product_menu(manager: ProductManager) -> None:
    """Меню добавления нового продукта."""
    print("\n--- Добавление нового элемента ---")
    print("Выберите тип продукта:")
    print("1. Фрукт")
    print("2. Молочная продукция")
    print("3. Мясо")
    
    choice = input("Ваш выбор (1-3): ").strip()
    
    if choice == '1':
        # Добавление фрукта
        name = input_string("Введите название фрукта: ")
        
        valid, msg = Product.validate_name(name)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        price = input_number("Введите цену (руб): ", min_val=0, max_val=1000000)
        valid, msg = Product.validate_price(price)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        origin = input_string("Введите страну происхождения: ")
        valid, msg = Fruit.validate_origin(origin)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        weight = input_number("Введите вес (г): ", min_val=0.1, max_val=10000)
        valid, msg = Fruit.validate_weight(weight)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        fruit = Fruit(name=name, price=price, origin=origin, weight=weight)
        manager.add_product(fruit)
        print("Фрукт успешно добавлен!")
        
    elif choice == '2':
        # Добавление молочной продукции
        name = input_string("Введите название продукта: ")
        
        valid, msg = Product.validate_name(name)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        price = input_number("Введите цену (руб): ", min_val=0, max_val=1000000)
        valid, msg = Product.validate_price(price)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        fat_content = input_number("Введите жирность (%): ", min_val=0, max_val=100)
        valid, msg = DairyProduct.validate_fat_content(fat_content)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        expiration_days = input_number("Введите срок годности (дней): ", min_val=0, max_val=3650, is_int=True)
        valid, msg = DairyProduct.validate_expiration_days(expiration_days)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        dairy = DairyProduct(name=name, price=price, fat_content=fat_content, expiration_days=expiration_days)
        manager.add_product(dairy)
        print("Молочный продукт успешно добавлен!")
        
    elif choice == '3':
        # Добавление мяса
        name = input_string("Введите название продукта: ")
        
        valid, msg = Product.validate_name(name)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        price = input_number("Введите цену (руб): ", min_val=0, max_val=1000000)
        valid, msg = Product.validate_price(price)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        animal_type = input_string("Введите тип животного: ")
        valid, msg = Meat.validate_animal_type(animal_type)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        protein = input_number("Введите содержание белка (г): ", min_val=0, max_val=100)
        valid, msg = Meat.validate_protein(protein)
        if not valid:
            print(f"Ошибка: {msg}")
            return
        
        meat = Meat(name=name, price=price, animal_type=animal_type, protein=protein)
        manager.add_product(meat)
        print("Мясной продукт успешно добавлен!")
        
    else:
        print("Неверный выбор")


def remove_product_menu(manager: ProductManager) -> None:
    """Меню удаления продукта по индексу."""
    print("\n--- Удаление элемента по индексу ---")
    
    if manager.size() == 0:
        print("Коллекция пуста")
        return
    
    print(f"В коллекции {manager.size()} элементов")
    index = input_number("Введите индекс для удаления (0-" + str(manager.size()-1) + "): ", 
                         min_val=0, max_val=manager.size()-1, is_int=True)
    
    if manager.remove_by_index(index):
        print(f"Элемент с индексом {index} успешно удален")
    else:
        print("Ошибка при удалении элемента")


def display_all_products(manager: ProductManager) -> None:
    """Вывод всех элементов в терминал."""
    print("\n--- Все элементы коллекции ---")
    
    products = manager.get_all_products()
    
    if len(products) == 0:
        print("Коллекция пуста")
        return
    
    for i, product in enumerate(products):
        print(f"[{i}] {product.get_type()}: {product.to_string()}")


def compare_elements_menu(manager: ProductManager) -> None:
    """Меню сравнения двух элементов на равенство."""
    print("\n--- Сравнение двух элементов на равенство ---")
    
    if manager.size() < 2:
        print("Для сравнения необходимо минимум 2 элемента в коллекции")
        return
    
    print(f"В коллекции {manager.size()} элементов")
    
    index1 = input_number("Введите индекс первого элемента (0-" + str(manager.size()-1) + "): ", 
                          min_val=0, max_val=manager.size()-1, is_int=True)
    index2 = input_number("Введите индекс второго элемента (0-" + str(manager.size()-1) + "): ", 
                          min_val=0, max_val=manager.size()-1, is_int=True)
    
    result = manager.compare_by_index(index1, index2)
    
    if result is not None:
        if result:
            print(f"Элементы с индексами {index1} и {index2} РАВНЫ")
        else:
            print(f"Элементы с индексами {index1} и {index2} НЕ равны")
    else:
        print("Ошибка при сравнении элементов")


def main_menu() -> None:
    """Главное меню приложения."""
    manager = ProductManager()
    
    while True:
        print("\n" + "=" * 40)
        print("       МЕНЮ ПРИЛОЖЕНИЯ")
        print("=" * 40)
        print("1. Добавить новый элемент")
        print("2. Удалить элемент по индексу")
        print("3. Вывод всех элементов")
        print("4. Сравнение двух элементов на равенство")
        print("5. Завершение работы")
        print("=" * 40)
        
        choice = input("Выберите пункт меню (1-5): ").strip()
        
        if choice == '1':
            add_product_menu(manager)
        elif choice == '2':
            remove_product_menu(manager)
        elif choice == '3':
            display_all_products(manager)
        elif choice == '4':
            compare_elements_menu(manager)
        elif choice == '5':
            print("Завершение работы приложения. До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт от 1 до 5.")


if __name__ == "__main__":
    main_menu()
