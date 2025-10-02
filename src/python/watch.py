
import time
from pathlib import Path
from main import build_all_pages

def watch_templates():
    """Отслеживает изменения в папке templates и автоматически пересобирает страницы"""
    templates_dir = Path(__file__).parent.parent / "templates"
    last_modified = {}
    
    print(f"Отслеживание изменений в {templates_dir}")
    print("Нажмите Ctrl+C для остановки")
    
    
    for file_path in templates_dir.glob("*.html"):
        last_modified[file_path] = file_path.stat().st_mtime
    
    try:
        while True:
            time.sleep(1)
            
            rebuild_needed = False
            current_files = list(templates_dir.glob("*.html"))
            
        
            for file_path in current_files:
                current_mtime = file_path.stat().st_mtime
                if file_path not in last_modified or last_modified[file_path] != current_mtime:
                    print(f"Обнаружено изменение в {file_path.name}")
                    last_modified[file_path] = current_mtime
                    rebuild_needed = True
            
        
            for file_path in current_files:
                if file_path not in last_modified:
                    print(f"Обнаружен новый файл: {file_path.name}")
                    last_modified[file_path] = file_path.stat().st_mtime
                    rebuild_needed = True
            
        
            for file_path in list(last_modified.keys()):
                if file_path not in current_files:
                    print(f"Файл {file_path.name} был удален")
                    del last_modified[file_path]
                    rebuild_needed = True
            
        
            if rebuild_needed:
                print("Пересборка страниц...")
                build_all_pages()
                print("Отслеживание продолжается...")
                
    except KeyboardInterrupt:
        print("\nОстановка отслеживания")

if __name__ == "__main__":
    watch_templates()