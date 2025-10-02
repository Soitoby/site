import os

def generate_menu_html():
    # Путь к папке с меню
    menu_path = "src/img/menu"
    
    # Проверяем существование папки
    if not os.path.exists(menu_path):
        print(f"Ошибка: Папка {menu_path} не существует!")
        return
    
    # Получаем список всех папок в директории меню
    try:
        folders = [f for f in os.listdir(menu_path) 
                  if os.path.isdir(os.path.join(menu_path, f))]
    except Exception as e:
        print(f"Ошибка при чтении папки: {e}")
        return
    
    # Сортируем папки по имени
    folders.sort()
    
    # Генерируем HTML-структуру
    html_content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Меню</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            padding: 20px;
        }
        .menu-container {
            max-width: 1200px;
            margin: 0 auto;
            
            border-radius: 10px;
            
            padding: 30px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        .category {
            margin-bottom: 30px;
            border-radius: 8px;
            overflow: hidden;
        }
        .category-header {            
            color: black;
            padding: 15px 20px;
            font-size: 1.4em;
            font-weight: bold;
        }
        .items-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 15px;
            padding: 20px;
        }
        .menu-item {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 6px;
            padding: 15px;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .menu-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .item-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 4px;
            margin-bottom: 10px;
        }
        .item-name {
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }
        .no-items {
            grid-column: 1 / -1;
            text-align: center;
            color: #6c757d;
            padding: 20px;
            font-style: italic;
        }
        @media (max-width: 768px) {
            .items-container {
                grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            }
            .menu-container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="menu-container">
        <h1>Меню</h1>
"""
    
    # Обрабатываем каждую папку как категорию меню
    for folder in folders:
        category_path = os.path.join(menu_path, folder)
        
        # Получаем все файлы в папке категории
        try:
            items = [f for f in os.listdir(category_path) 
                    if os.path.isfile(os.path.join(category_path, f))]
            
            # Фильтруем только изображения (можно расширить список форматов)
            image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}
            items = [item for item in items 
                    if os.path.splitext(item)[1].lower() in image_extensions]
            
        except Exception as e:
            print(f"Ошибка при чтении папки {folder}: {e}")
            items = []
        
        # Добавляем категорию в HTML
        html_content += f"""
        <div class="category">
            <div class="category-header">{folder}</div>
            <div class="items-container">
        """
        
        # Добавляем позиции меню (файлы) в категорию
        if items:
            for item in sorted(items):
                item_name = os.path.splitext(item)[0]  # Убираем расширение файла
                item_path = os.path.join(menu_path, folder, item).replace('\\', '/')
                
                html_content += f"""
                
                    <img src="/{item_path}" alt="{item_name}" class="item-image" onerror="this.style.display='none'">
                    
                
                """
        else:
            html_content += '<div class="no-items">Позиции временно отсутствуют</div>'
        
        html_content += """
            </div>
        </div>
        """
    
    html_content += """
    </div>
    <script>
        // Добавляем обработку ошибок загрузки изображений
        document.addEventListener('DOMContentLoaded', function() {
            const images = document.querySelectorAll('.item-image');
            images.forEach(img => {
                img.onerror = function() {
                    this.style.display = 'none';
                    const itemName = this.nextElementSibling;
                    if (itemName) {
                        itemName.style.marginTop = '20px';
                    }
                };
            });
        });
    </script>
</body>
</html>"""
    
    # Сохраняем HTML-файл
    try:
        with open('src/templates/menu.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("✅ Меню успешно создано в файле menu.html")
        print(f"📁 Обработано категорий: {len(folders)}")
    except Exception as e:
        print(f"❌ Ошибка при сохранении файла: {e}")

def start_manu_create():
    generate_menu_html()