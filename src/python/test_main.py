# main.py
import fastapi
import os
from pathlib import Path

# Создаем директории если не существуют
Path("src/html").mkdir(parents=True, exist_ok=True)

# Пути к шаблонам
HEADER = "src/templates/header.html" 
FOOTER = "src/templates/footer.html"

def read_template(path_template: str):
    """Читает шаблон из файла"""
    with open(path_template, "r", encoding='utf-8') as f:
        return f.read()
     
def create_page(template_path: str, output_name: str):
    """Создает HTML-страницу из шаблонов"""
    header = read_template(HEADER)
    content = read_template(template_path)
    footer = read_template(FOOTER)    
    with open(f"src/html/{output_name}", "w", encoding="utf-8") as f:
        f.write(header + content + footer)

app = fastapi.FastAPI()

@app.get("/")
async def root():
    """Корневой маршрут - перенаправляет на главную страницу"""
    return await main_page()

@app.get("/main")
async def main_page():
    """Главная страница"""
    page = "main.html"
    file_path = f"src/html/{page}"
    template_path = "src/templates/main.html"
    
    if not os.path.isfile(file_path) and os.path.isfile(template_path):
        create_page(template_path, page)
    
    if os.path.isfile(file_path):
        return fastapi.responses.FileResponse(file_path)
    else:
        return fastapi.responses.HTMLResponse("Page not found", status_code=404)

@app.get("/menu")
async def menu_page():
    """Страница меню"""
    page = "menu.html"
    file_path = f"src/html/{page}"
    template_path = "src/templates/menu.html"
    
    if not os.path.isfile(file_path) and os.path.isfile(template_path):
        create_page(template_path, page)
    
    if os.path.isfile(file_path):
        return fastapi.responses.FileResponse(file_path)
    else:
        return fastapi.responses.HTMLResponse("Page not found", status_code=404)

@app.get("/contact")
async def contact_page():
    """Страница контактов"""
    page = "contact.html"
    file_path = f"src/html/{page}"
    template_path = "src/templates/contact.html"
    
    if not os.path.isfile(file_path) and os.path.isfile(template_path):
        create_page(template_path, page)
    
    if os.path.isfile(file_path):
        return fastapi.responses.FileResponse(file_path)
    else:
        return fastapi.responses.HTMLResponse("Page not found", status_code=404)

@app.get("/about")
async def about_page():
    """Страница 'О нас'"""
    page = "about.html"
    file_path = f"src/html/{page}"
    template_path = "src/templates/about.html"
    
    if not os.path.isfile(file_path) and os.path.isfile(template_path):
        create_page(template_path, page)
    
    if os.path.isfile(file_path):
        return fastapi.responses.FileResponse(file_path)
    else:
        return fastapi.responses.HTMLResponse("Page not found", status_code=404)