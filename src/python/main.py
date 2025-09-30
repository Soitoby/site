import fastapi, jinja2

HEADER = "src\templates\header.html" 
FOOTER = "src\templates\footer.html"

def read_templates(path_template:str):
    with open(path_template,"r", encoding='utf-8') as f:
        return f.read()
     
def create_pages(content):


def main():
    app = fastapi.FastAPI()
    @app.get("/")
    async def main_page(main_page:str):
        return main_page


if __name__ =="__main__":
    main()

