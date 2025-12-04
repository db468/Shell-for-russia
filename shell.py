import time
import platform
import os
import subprocess

while True:
    print("Shell 1.4, All products safety")
    enter = input(">>> ")

    if enter == "/del":
        filename = input("Укажите имя файла (его расширением например: txt): ")
        time.sleep(2)
        try:
            os.remove(filename)
            print(f"Файл '{filename}' успешно удалён.")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
        except PermissionError:
            print(f"нет прав на удаление файла '{filename}'.")     

    if enter == "/help":
        print("Под shell поддерживаются пакеты, чтобы их получить введите:")
        print("sudo install ppk (имя_файла).")
        print("В shell поддерживаются приложения, чтобы их открыть введите:")
        print("sudo app start (имя приложения)")
        print("Базовые команды:")
        print("/del - удалить файл")
        print("/notepad - открыть блокнот")
        print("/off - выключить систему")
        print("/exit - выключить командную строку")
        continue

    elif enter == "/off":
        gg = input("Вы действительно хотите продолжить? (y/n): ")
        if gg.lower() == "y":
            system_name = platform.system()
            if system_name == "Windows":
                os.system("shutdown /s /t 1")
            elif system_name == "Linux":
                os.system("sudo shutdown -h now")
            else:
                print("Команда выключения для вашей ОС не определена.")
        elif gg.lower() == "n":
            print("Администратор прервал выключение системы.")
            continue
    if enter == "sudo app start":
        # Запрашиваем путь к приложению
      path_to_app = input("Введите полный путь к приложению: ")

    # Проверяем существование файла
      if os.path.exists(path_to_app):
        try:
            # Пытаемся запустить
            subprocess.Popen([path_to_app])
            print("Приложение запущено.")
        except Exception as e:
            print(f"Не удалось запустить приложение: {e}")
    else:
        print("Файл по указанному пути не найден.")
 
    if enter == "/exit":
        if input("Вы действительно хотите выйти? Все работающие процессы через shell будут выключенны (y/n): ") == "y":
            break
        else:
            print("Операция была прерванна администратором")
    
