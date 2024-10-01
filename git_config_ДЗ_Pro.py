# Импортируем библиотеку subprocess
import subprocess

# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
def git_config_list():
    # Удаляем заглушку, создаем переменную result:
    # Используем subprocess.run для выполнения команды в переменной result
    # Выводим результат выполнения команды result.stdout
    result = subprocess.run(['git', 'config', '--list'], capture_output=True, text=True)
    print(result.stdout)
    

# вызываем git_config_list()
git_config_list()
