# src/python/main.py
import os
from pathlib import Path

# Определяем пути относительно расположения скрипта
BASE_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
HTML_OUTPUT_DIR = BASE_DIR / "html"
CSS_DIR = BASE_DIR / "css"
IMG_DIR = BASE_DIR / "img"

def read_template(template_path):
    """Читает содержимое шаблона из файла"""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {template_path} не найден")
        return ""
    except Exception as e:
        print(f"Ошибка при чтении файла {template_path}: {e}")
        return ""

def build_page(template_name, output_name=None):
    """Собирает страницу из шаблонов"""
    if output_name is None:
        output_name = template_name
    
    # Пути к файлам
    header_path = TEMPLATES_DIR / "header.html"
    footer_path = TEMPLATES_DIR / "footer.html"
    content_path = TEMPLATES_DIR / template_name
    output_path = HTML_OUTPUT_DIR / output_name
    
    # Проверяем существование необходимых файлов
    if not header_path.exists():
        print(f"Ошибка: файл header.html не найден в {TEMPLATES_DIR}")
        return False
    
    if not footer_path.exists():
        print(f"Ошибка: файл footer.html не найден в {TEMPLATES_DIR}")
        return False
    
    if not content_path.exists():
        print(f"Ошибка: файл {template_name} не найден в {TEMPLATES_DIR}")
        return False
    
    # Читаем шаблоны
    header = read_template(header_path)
    content = read_template(content_path)
    footer = read_template(footer_path)
    
    if not header or not content or not footer:
        print("Ошибка: один из шаблонов пуст или не может быть прочитан")
        return False
    
    # Объединяем шаблоны
    full_page = header + content + footer
    
    # Сохраняем результат
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_page)
        print(f"Страница {output_name} успешно собрана и сохранена в {output_path}")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении страницы {output_name}: {e}")
        return False

def build_all_pages():
    """Собирает все страницы из шаблонов"""
    # Создаем выходную директорию, если она не существует
    HTML_OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Получаем список всех HTML-файлов в папке templates, кроме header и footer
    template_files = [f for f in os.listdir(TEMPLATES_DIR) 
                     if f.endswith('.html') and f not in ['header.html', 'footer.html']]
    
    if not template_files:
        print(f"В папке {TEMPLATES_DIR} не найдено HTML-файлов для сборки")
        return
    
    print(f"Найдено {len(template_files)} файлов для сборки: {', '.join(template_files)}")
    
    # Собираем каждую страницу
    success_count = 0
    for template_file in template_files:
        if build_page(template_file):
            success_count += 1
    
    print(f"Успешно собрано {success_count} из {len(template_files)} страниц")

def check_directories():
    """Проверяет существование необходимых директорий"""
    directories = [TEMPLATES_DIR, CSS_DIR, IMG_DIR]
    missing_dirs = []
    
    for directory in directories:
        if not directory.exists():
            missing_dirs.append(directory.name)
            print(f"Предупреждение: директория {directory} не найдена")
    
    if missing_dirs:
        print(f"Отсутствуют следующие директории: {', '.join(missing_dirs)}")
        print("Создайте их для правильной работы проекта")
    
    return len(missing_dirs) == 0

def start_create_page():
    print("Начинаем сборку страниц из шаблонов...")
    
    # Проверяем директории
    if not check_directories():
        print("Продолжаем сборку, но некоторые ресурсы могут быть недоступны")
    
    # Собираем все страницы
    build_all_pages()
    
    print("Сборка завершена!")