from PIL import Image
import timeit

# Загрузка изображения
image_path = "1.jpg"
original_image = Image.open(image_path)
im = Image.open(image_path)
(width, height) = im.size
# Перед удалением красного канала, убедимся, что изображение имеет режим "RGB"
if original_image.mode != "RGB":
    original_image = original_image.convert("RGB")

# Удаление красного канала
def remove_red_channel(image):
    r, g, b = image.split()
    return Image.merge("RGB", (r.point(lambda i: i*0), g, b))

# Засекаем время выполнения
execution_time = timeit.timeit(lambda: remove_red_channel(original_image), number=1)

# Удаление красного канала
result_image = remove_red_channel(original_image)

# Сохранение нового файла
result_image.save("output_image.jpg")

print(f"Удаление красного канала заняло {execution_time:.2f} секунд")
print(width, height)
# Освобождаем ресурсы
original_image.close()
result_image.close()