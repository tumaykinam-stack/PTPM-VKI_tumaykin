import logging
import sys
from math import sqrt

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('triangle_calculator.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Проверяет, является ли тройка сторон действительным треугольником."""
    return a + b > c and a + c > b and b + c > a

def determine_triangle_type(a: float, b: float, c: float) -> str:
    """Определяет тип треугольника по длинам сторон."""
    if not is_valid_triangle(a, b, c):
        return "не треугольник"
    if a == b == c:
        return "равносторонний"
    if a == b or b == c or a == c:
        return "равнобедренный"
    return "разносторонний"

def calculate_coordinates() -> list:
    """Вычисляет координаты вершин треугольника."""
    # Вершины треугольника в поле 100x100
    return [(0, 0), (100, 0), (50, int(sqrt(3) * 50))]

def main():
    # Получение входных данных
    sides = []
    for i in range(1, 4):
        side = input(f"Введите длину стороны {chr(64 + i)}: ")
        try:
            side_length = float(side)
            if side_length <= 0:
                raise ValueError("Длина стороны должна быть положительной.")
            sides.append(side_length)
        except ValueError as e:
            logging.error(f"Ошибка ввода для стороны {i}: {side}. Ошибка: {e}")
            sides.append(-2)  # Устанавливаем значение для некорректного ввода

    # Обработка введенных сторон
    if -2 in sides:
        coordinates = [(-2, -2)] * 3
        triangle_type = ""
    else:
        a, b, c = sides
        triangle_type = determine_triangle_type(a, b, c)
        if triangle_type == "не треугольник":
            coordinates = [(-1, -1)] * 3
        else:
            coordinates = calculate_coordinates()

    # Логируем результат
    logging.info(f"Входные данные: {sides}, Тип треугольника: {triangle_type}, Координаты: {coordinates}")

    # Вывод результата
    print(f"Тип треугольника: {triangle_type}")
    print(f"Координаты вершин: {coordinates}")

if __name__ == "__main__":
    main()