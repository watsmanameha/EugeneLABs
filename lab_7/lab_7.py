from PIL import Image
import numpy as np
import numba
import timeit

# Загрузка изображения
image_path = "1.jpg"
original_image = Image.open(image_path)
im = Image.open(image_path)
(width, height) = im.size
# Перед удалением красного канала, убедимся, что изображение имеет режим "RGB"
if original_image.mode != "RGB":
    original_image = original_image.convert("RGB")

# Удаление красного канала в верхней части изображения с использованием Numba
@numba.njit(parallel=True)
def remove_red_channel_numba(image_array):
    for x in numba.prange(width):
        for y in numba.prange(height):
            # Проверяем, находится ли пиксель выше или на диагонали
            if y <= x * height / width:
                image_array[y, x, 0] = 0  # Устанавливаем красный канал в 0

# Преобразование изображения в массив NumPy
img_array = np.array(original_image)

# Засекаем время выполнения с Numba
execution_time_numba = timeit.timeit(lambda: remove_red_channel_numba(img_array), number=1)

# Преобразование обратно в изображение
result_image_numba = Image.fromarray(img_array)

# Сохранение нового файла
result_image_numba.save("output_image_numba.jpg")

print(f"Удаление красного канала с использованием Numba заняло {execution_time_numba:.2f} секунд")
print(width, height)
# Освобождаем ресурсы
original_image.close()
result_image_numba.close()
