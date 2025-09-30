# conftest.py
import pytest
import sys
import os

# Добавляем корневую директорию в PYTHONPATH для импорта модулей
sys.path.insert(0, os.path.dirname(__file__))