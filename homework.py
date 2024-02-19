import os
import logging
from collections import namedtuple

# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Определение объекта namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_info(directory_path):
    """
    Функция для получения информации о содержимом директории.
    :param directory_path: Путь до директории.
    :return: Список объектов FileInfo.
    """
    directory_info = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        name, extension = os.path.splitext(item)
        is_directory = os.path.isdir(item_path)
        parent_directory = os.path.basename(os.path.dirname(item_path))
        file_info = FileInfo(name=name, extension=extension if not is_directory else None,
                             is_directory=is_directory, parent_directory=parent_directory)
        directory_info.append(file_info)
        logging.info(f'Name: {name}, Extension: {extension if not is_directory else "None"}, '
                     f'Is Directory: {is_directory}, Parent Directory: {parent_directory}')
    return directory_info

if __name__ == "__main__":
    import sys
    
    # Получаем путь до директории из командной строки
    if len(sys.argv) != 2:
        print("Usage: python script.py directory_path")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    # Проверка существования директории
    if not os.path.isdir(directory_path):
        print("Error: Directory not found.")
        sys.exit(1)
    
    # Получаем информацию о директории и сохраняем ее в файл
    directory_info = get_directory_info(directory_path)
    print("Directory information has been logged to directory_info.log file.")
