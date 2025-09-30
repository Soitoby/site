import fastapi
import os
from pathlib import Path

# Создаем директорию если не существует
Path("src/html").mkdir(parents=True, exist_ok=True)

HEADER = "src/templates/header.html" 
FOOTER = "src/templates/footer.html"
ABOUT = "src/templates/about.html"
CONTACT = "src/templates/contact.html"
MAIN = "src/templates/main.html"
MENU = "src/templates/menu.html"
INDEX = "src/templates/main.html"

def read_template(path_template: str):
    try:
        with open(path_template, "r", encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading template {path_template}: {e}")
        return ""
     
def create_page(template_path: str, output_name: str):
    header = read_template(HEADER)
    content = read_template(template_path)
    footer = read_template(FOOTER)
    if content == "":
        return False
    try:
        with open(f"src/html/{output_name}", "w", encoding="utf-8") as f:
            f.write(header + content + footer)
        return True
    except Exception as e:
        print(f"Error creating page {output_name}: {e}")
        return False

app = fastapi.FastAPI()

@app.get("/")
async def root():
    page = "index.html"
    file_path = f"src/html/{page}"
    
    if not os.path.isfile(file_path):
        if os.path.isfile(INDEX):
            if create_page(INDEX, page):
                return fastapi.responses.FileResponse(file_path)
            else:
                return fastapi.responses.HTMLResponse("Error creating page", status_code=500)
        else:
            return fastapi.responses.HTMLResponse("Index template not found", status_code=404)
    return fastapi.responses.FileResponse(file_path)

@app.get("/main")
async def main_page():
    page = "main.html"
    file_path = f"src/html/{page}"
    
    if not os.path.isfile(file_path):
        if os.path.isfile(MAIN):
            if create_page(MAIN, page):
                return fastapi.responses.FileResponse(file_path)
            else:
                return fastapi.responses.HTMLResponse("Error creating page", status_code=500)
        else:
            return fastapi.responses.HTMLResponse("Template not found", status_code=404)
    
    return fastapi.responses.FileResponse(file_path)

@app.get("/menu")
async def menu_page():
    page = "menu.html"
    file_path = f"src/html/{page}"
    
    if not os.path.isfile(file_path):
        if os.path.isfile(MENU):
            if create_page(MENU, page):
                return fastapi.responses.FileResponse(file_path)
            else:
                return fastapi.responses.HTMLResponse("Error creating page", status_code=500)
        else:
            return fastapi.responses.HTMLResponse("Template not found", status_code=404)
    
    return fastapi.responses.FileResponse(file_path)

@app.get("/contact")
async def contact_page():
    page = "contact.html"
    file_path = f"src/html/{page}"
    
    if not os.path.isfile(file_path):
        if os.path.isfile(CONTACT):
            if create_page(CONTACT, page):
                return fastapi.responses.FileResponse(file_path)
            else:
                return fastapi.responses.HTMLResponse("Error creating page", status_code=500)
        else:
            return fastapi.responses.HTMLResponse("Template not found", status_code=404)
    
    return fastapi.responses.FileResponse(file_path)

@app.get("/about")
async def about_page():
    page = "about.html"
    file_path = f"src/html/{page}"
    
    if not os.path.isfile(file_path):
        if os.path.isfile(ABOUT):
            if create_page(ABOUT, page):
                return fastapi.responses.FileResponse(file_path)
            else:
                return fastapi.responses.HTMLResponse("Error creating page", status_code=500)
        else:
            return fastapi.responses.HTMLResponse("Template not found", status_code=404)
    
    return fastapi.responses.FileResponse(file_path)