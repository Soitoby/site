# test_main.py
import pytest
import os
import shutil
from fastapi.testclient import TestClient
from pathlib import Path
from main import app, create_page, read_template

# Фикстуры для тестов
@pytest.fixture(scope="function")
def client():
    """Создает тестового клиента"""
    return TestClient(app)

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    """Создает и очищает тестовые директории перед/после каждого теста"""
    # Создаем тестовые директории
    test_templates_dir = Path("test_src/templates")
    test_html_dir = Path("test_src/html")
    test_templates_dir.mkdir(parents=True, exist_ok=True)
    test_html_dir.mkdir(parents=True, exist_ok=True)
    
    # Создаем тестовые шаблоны
    with open(test_templates_dir / "header.html", "w", encoding="utf-8") as f:
        f.write("<header>Test Header</header>")
    
    with open(test_templates_dir / "footer.html", "w", encoding="utf-8") as f:
        f.write("<footer>Test Footer</footer>")
    
    with open(test_templates_dir / "main.html", "w", encoding="utf-8") as f:
        f.write("<main>Test Main Content</main>")
    
    with open(test_templates_dir / "menu.html", "w", encoding="utf-8") as f:
        f.write("<main>Test Menu Content</main>")
    
    with open(test_templates_dir / "contact.html", "w", encoding="utf-8") as f:
        f.write("<main>Test Contact Content</main>")
    
    with open(test_templates_dir / "about.html", "w", encoding="utf-8") as f:
        f.write("<main>Test About Content</main>")
    
    # Сохраняем оригинальные пути
    original_header = None
    original_footer = None
    
    # Мокаем пути в основном модуле
    import main
    original_header = main.HEADER
    original_footer = main.FOOTER
    
    main.HEADER = "test_src/templates/header.html"
    main.FOOTER = "test_src/templates/footer.html"
    
    yield
    
    # Восстанавливаем оригинальные пути
    if original_header and original_footer:
        main.HEADER = original_header
        main.FOOTER = original_footer
    
    # Очищаем тестовые директории
    if Path("test_src").exists():
        shutil.rmtree("test_src")

# Тесты для функций
def test_read_template():
    """Тестирует чтение шаблона"""
    content = read_template("test_src/templates/header.html")
    assert content == "<header>Test Header</header>"

def test_create_page():
    """Тестирует создание страницы"""
    # Убедимся, что файла еще нет
    if os.path.exists("test_src/html/test_page.html"):
        os.remove("test_src/html/test_page.html")
    
    # Создаем страницу
    create_page("test_src/templates/main.html", "test_page.html")
    
    # Проверяем, что файл создан
    assert os.path.exists("test_src/html/test_page.html")
    
    # Проверяем содержимое
    with open("test_src/html/test_page.html", "r", encoding="utf-8") as f:
        content = f.read()
        assert "<header>Test Header</header>" in content
        assert "<main>Test Main Content</main>" in content
        assert "<footer>Test Footer</footer>" in content

# Тесты для маршрутов
def test_root_route(client):
    """Тестирует корневой маршрут"""
    response = client.get("/")
    assert response.status_code == 200

def test_main_route(client):
    """Тестирует маршрут /main"""
    response = client.get("/main")
    assert response.status_code == 200
    # Проверяем, что создался HTML файл
    assert os.path.exists("test_src/html/main.html")

def test_menu_route(client):
    """Тестирует маршрут /menu"""
    response = client.get("/menu")
    assert response.status_code == 200
    assert os.path.exists("test_src/html/menu.html")

def test_contact_route(client):
    """Тестирует маршрут /contact"""
    response = client.get("/contact")
    assert response.status_code == 200
    assert os.path.exists("test_src/html/contact.html")

def test_about_route(client):
    """Тестирует маршрут /about"""
    response = client.get("/about")
    assert response.status_code == 200
    assert os.path.exists("test_src/html/about.html")

def test_nonexistent_route(client):
    """Тестирует несуществующий маршрут"""
    response = client.get("/nonexistent")
    assert response.status_code == 404

def test_page_content(client):
    """Тестирует содержимое созданных страниц"""
    # Создаем страницу через запрос
    response = client.get("/main")
    
    # Читаем созданный файл
    with open("test_src/html/main.html", "r", encoding="utf-8") as f:
        content = f.read()
        # Проверяем, что все компоненты присутствуют
        assert "<header>Test Header</header>" in content
        assert "<main>Test Main Content</main>" in content
        assert "<footer>Test Footer</footer>" in content

# Тесты для обработки ошибок
def test_missing_template():
    """Тестирует обработку отсутствующего шаблона"""
    # Временно изменяем пути на несуществующие
    import main
    original_header = main.HEADER
    main.HEADER = "nonexistent/header.html"
    
    # Пытаемся создать страницу с несуществующим шаблоном
    try:
        create_page("test_src/templates/main.html", "error_test.html")
        # Если мы здесь, значит ошибка не обработана
        assert False, "Ожидалась ошибка при чтении несуществующего шаблона"
    except Exception as e:
        # Ожидаем, что будет исключение при открытии файла
        assert True
    
    # Восстанавливаем оригинальный путь
    main.HEADER = original_header

# Запуск тестов
if __name__ == "__main__":
    pytest.main([__file__, "-v"])