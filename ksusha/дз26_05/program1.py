class Product:
    def __init__(self, name_product: str, name_shop: str, price: int) -> None:
        self.name_product = name_product
        self.name_shop = name_shop
        self.price = price
        obj.add_product(self)

    def __add__(self, other: 'Product') -> int:
        return self.price + other.price


class Warehouse():
    def __init__(self, name: str) -> None:
        self.name = name
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def print_inf(self, i: int) -> None:
        print(f"Название товара: {self.products[i].name_product}")
        print(f"Цена товара: {self.products[i].price}")
        print(f"Магазин, в котором продаётся товар: {self.products[i].name_shop}")

    def information_about_the_index(self, i: int) -> None:
        self.print_inf(i)

    def name_information(self, name: str) -> None:
        for product in range(len(self.products)):
            if self.products[product].name_product == name:
                self.print_inf(product)                

    def sort_price(self) -> None:
        sorted_products = sorted(self.products, key=lambda p: p.price)
        for product in sorted_products:
            print(f"Название товара: {product.name_product}, цена: {product.price}")

    def sort_name(self) -> None:
        sorted_products = sorted(self.products, key=lambda p: p.name_product)
        for product in sorted_products:
            print(f"Название товара: {product.name_product}")

    def sort_shop(self) -> None:
        sorted_products = sorted(self.products, key=lambda p: p.name_shop)
        for product in sorted_products:
            print(f"Название товара: {product.name_product}, магазин {product.name_shop}")


obj = Warehouse("ddd")
f = Product("Хлеб", "Пятёрочка", 35)
d = Product("Молоко", "Магнит", 80)
Product("Масло сливочное", "ВкусВилл", 150)
Product("Сыр Российский", "Перекрёсток", 250)
Product("Колбаса Докторская", "Пятёрочка", 180)
Product("Яйца куриные", "Магнит", 95)
Product("Печенье", "Дикси", 45)
Product("Вода питьевая", "Пятёрочка", 30)
Product("Сок апельсиновый", "ВкусВилл", 120)
Product("Шоколад", "Магнит", 65)
