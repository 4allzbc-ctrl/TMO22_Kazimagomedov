"""
Вариант 9  Файлов в папке
Функция: files_per_folder(files, folders). Число файлов разделите на число папок. Пример: files_per_folder(48, 6) → 8.0.
Слова для сортировки: ["лук", "морковь", "картофель"]
"""


def files_per_folder(files, folders):
    if folders == 0:
        return "На ноль делить нельзя"
    return files / folders


assert files_per_folder(48, 6)
assert files_per_folder(48, 0)
assert files_per_folder(56, 8)

words = ["лук", "морковь", "картофель"]
sorted_words = sorted(words, key=len)
print(sorted_words)
