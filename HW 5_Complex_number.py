import cmath
import numpy as np

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        try:
            module = np.round(cmath.polar(complex(self.real, self.imag))[0], 2)
            argument = np.round(cmath.polar(complex(self.real, self.imag))[1], 2)
            if self.real == 0 and self.imag == 0:
                raise ValueError("Невозможно представить в экспоненциальной форме: нулевое число")
            return f'z = {self.real} + {self.imag}j = {module} * exp(j*{argument})'
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"Ошибка: {e}"

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)
        else:
            raise TypeError("Сложение возможно только с комплексными и вещественными числами")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)
        else:
            raise TypeError("Вычитание возможно только с комплексными и вещественными числами")

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)
        elif isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)
        else:
            raise TypeError("Умножение возможно только с комплексными и вещественными числами")

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denominator = other.real**2 + other.imag**2
            if denominator == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            return Complex((self.real * other.real + self.imag * other.imag) / denominator, (self.imag * other.real - self.real * other.imag) / denominator)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            return Complex(self.real / other, self.imag / other)
        else:
            raise TypeError("Деление возможно только на комплексные и вещественные числа")

    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.real == other.real and self.imag == other.imag
        return False

    @property
    def module(self):
        return np.round(cmath.polar(complex(self.real, self.imag))[0], 2)

#Функция калькулятора
def calculate():
    try:
        #Ввод данных
        real1 = float(input("Введите вещественную часть первого числа: "))
        imag1 = float(input("Введите мнимую часть первого числа: "))
        num1 = Complex(real1, imag1)

        real2 = float(input("Введите вещественную часть второго числа: "))
        imag2 = float(input("Введите мнимую часть второго числа: "))
        num2 = Complex(real2, imag2)
        
        #Выбор операции
        op = input("Выберите операцию (+, -, *, /): ")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            raise ValueError("Неверная операция")
        
        print(result)

    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Ошибка: {e}")

calculate()