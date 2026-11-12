# Вариант 9

# Задание 1
print("Задание 1.\n")
g = (num + 9 for num in [1, 2, 3])
print(list(g))

print("\n\nЗадание 2.\n")


# Задание 2
def announce(func):
    def wrapper(*args, **kwargs):
        print("Приветствуем")
        result = func(*args, **kwargs)
        print("Готово")
        return result

    return wrapper


@announce
def hello():
    print("Привет!")


hello()
