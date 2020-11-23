import sys
import numpy as np
from PIL import Image

# Вказуємо розмір зображення
WIDTH = 540
HEIGHT = 960

# Кол вказується у форматі Red Green Blue, тобто займає
# 3 числа якщо зберігати їх у списку
RGB = 3

# Колір фона - чорный
# Колір точок - білий
BG_COLOR = [255, 255, 255]
TEXT_COLOR = [0, 0, 0]

# Шлях до файлу вказується або при виклику програми (можна так само
# просто перетягнути датасет на іконку програми і воно спрацює)
# Або ж якщо нічого не вказувати, то за стандартом візьме 7-ий DS
try:
    file_path = sys.argv[1]
except Exception:
    file_path = "DS7.txt"

# Зберігається підсумковий результат під тим же ім'ям що і файл,
# тільки у форматі .png: DS7.txt -> DS7.png
save_path = file_path[:file_path.rfind('.') + 1] + 'png'

# Відкриваємо файл на зчитування
with open(file_path, 'r') as file:
    # Проходимся по рядках файлу, ділимо їх по пропуску, записуємо
    # координати в список у вигляді числа
    data = [[int(single_cord) for single_cord in line.split()] for line in file]

# Картинка це тривимірний масив який задається висотою,
# Шириною і форматом RGB
# Задається саме в такому порядку!
# Приклад кінцевого виду:
# [ #       x_0             x_1               x_width
#   [ [255, 255, 255], [0, 144, 131], ..., [100, 200, 0] ], # y_0
#   [ [255, 255, 255], [0, 144, 131], ..., [100, 200, 0] ], # y_1
#   ...
#   [ [255, 255, 255], [0, 144, 131], ..., [100, 200, 0] ]  # y_height
# ]
image_array = np.full([HEIGHT, WIDTH, RGB], BG_COLOR, dtype=np.uint8)

# Заповнюємо масив даними з датасета
for coords_pare in data:
    x = coords_pare[0]
    y = coords_pare[1]
    image_array[y][x] = TEXT_COLOR

# Перетворюємо масив в зображення у форматі RGB
img = Image.fromarray(image_array, 'RGB')
# Перевертаємо зображення в читабельний формат
img = img.rotate(90, expand=True)

# Показуємо зображення
img.show()
# Зберігаємо зображення
img.save(save_path)
