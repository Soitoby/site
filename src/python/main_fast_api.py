import fastapi
import fastapi.staticfiles
import main
import menu_create
import uvicorn


main.start_create_page()
menu_create.start_manu_create()

app = fastapi.FastAPI()
app.mount("/src/css", fastapi.staticfiles.StaticFiles(directory="src/css"), name="css")
app.mount("/src/img", fastapi.staticfiles.StaticFiles(directory="src/img"), name="img")
def read_html(path: str):
    """Читает HTML файл и возвращает его содержимое"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"<h1>Файл {path} не найден</h1>"
    except Exception as e:
        return f"<h1>Ошибка при чтении файла: {str(e)}</h1>"

@app.get("/")
async def root():
    return fastapi.responses.HTMLResponse(read_html("src/html/index.html"))

@app.get("/index")
async def index():
    return fastapi.responses.HTMLResponse(read_html("src/html/index.html"))

@app.get("/about")
async def about():
    return fastapi.responses.HTMLResponse(read_html("src/html/about.html"))

@app.get("/contact")
async def contact():
    return fastapi.responses.HTMLResponse(read_html("src/html/contact.html"))

@app.get("/menu")
async def menu():
    return fastapi.responses.HTMLResponse(read_html("src/html/menu.html"))


from fastapi.staticfiles import StaticFiles
import os


os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)