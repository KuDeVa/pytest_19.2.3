class Calculator:
    def multiply(self, x, y):  # умножение
        return x * y

    def division(self, x, y):  # разделить
        return x / y

    def subtraction(self, x, y):  # вычитание
        return x - y

    def adding(self, x, y):  # сложение
        return x + y

    def adding_multiply(self, x, y, z):  # сложение умножение
        return x + y * z

    def adding_subtraction_multiply(self, x, y, z, b):  # сложение вычитание умножение
        return x + y - z * b
