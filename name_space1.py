
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

test_function()

# Вызовите функцию inner_function вне функции test_function
    inner_function()

#получили ошибку, потому что inner_function не доступна
# в глобальной области видимости
