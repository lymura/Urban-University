class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return '\n'.join(line.strip() for line in file if line.strip())

    def add(self, *products):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                existing_products = {line.strip() for line in file if line.strip()}
        except FileNotFoundError:
            existing_products = set()

        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                product_str = str(product)
                if product_str not in existing_products:
                    file.write(product_str + '\n')
                    existing_products.add(product_str)


# Пример использования
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    s1.add(p1, p2, p3)

    print(s1.get_products())
