import fastapi, jinja2, os

HEADER = "src\templates/header.html" 
FOOTER = "src\templates/footer.html"

def read_templates(path_template:str):
    with open(path_template,"r", encoding='utf-8') as f:
        return f.read()
     
def create_pages(content:str, name:str):
    header = read_templates(HEADER)
    content = read_templates(content)
    footer = read_templates(FOOTER)    
    with open(f"src/html/{name}", "w",encoding="utf-8") as f:
        f.write(header + content + footer)


def Fastapi(app):
    
    @app.get("/")
    async def main_page(page:str):
        if os.path.isfile(f"src/html/{page}"):
            return fastapi.responses.FileResponse(page)
        else:
            create_pages(f"src/templates/{page}","{page}")
            return fastapi.responses.FileResponse(page)
        
    @app.get("/menu")
    async def menu_page(page:str):
        if os.path.isfile(f"src/html/{page}"):
            return fastapi.responses.FileResponse(page)
        else:
            create_pages(f"src/templates/{page}","{page}")
            return fastapi.responses.FileResponse(page)
        
    @app.get("/contact")
    async def contact_page(page:str):
        if os.path.isfile(f"src/html/{page}"):
            return fastapi.responses.FileResponse(page)
        else:
            create_pages(f"src\templates\{page}",f"{page}")
            return fastapi.responses.FileResponse(page)
    
    @app.get("/about")
    async def about_page(page:str):
        if os.path.isfile(f"src/html/{page}"):
            return fastapi.responses.FileResponse(page)
        else:
            create_pages(f"src\templates\{page}",f"{page}")
            return fastapi.responses.FileResponse(page)
        
def main():
    app = fastapi.FastAPI()
    while True:
        Fastapi(app)
    
    
    
        


if __name__ =="__main__":
    main()

