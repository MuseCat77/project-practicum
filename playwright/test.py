import re
from playwright.sync_api import Page, expect

def test_page_loads_and_has_title(page: Page):
    """Проверяем загрузку страницы и наличие заголовка"""
    page.goto("http://localhost:8050/")
    
    # Проверка основного заголовка
    expect(page.locator("text=Список процессоров")).to_be_visible()
    
    # Проверка наличия графика
    graph = page.locator("#graph")
    expect(graph).to_be_visible()
    
    # Скриншот всей страницы
    page.screenshot(path="playwright-tests/screenshots/page_loaded.png")

def test_dropdown_interaction(page: Page):
    """Тестируем работу выпадающего списка для графика"""
    page.goto("http://localhost:8050/")
    
    # Проверяем наличие dropdown
    dropdown = page.locator("#graph-dropdown")
    expect(dropdown).to_be_visible()
    
    # Проверяем выбранное значение по умолчанию
    selected_value = page.locator("#graph-dropdown .Select-value-label")
    expect(selected_value).to_have_text("vendor")
    
    # Меняем значение и проверяем обновление
    dropdown.click()
    page.locator(".VirtualizedSelectOption", has_text="type").click()
    
    # Проверяем новое выбранное значение
    updated_value = page.locator("#graph-dropdown .Select-value-label")
    expect(updated_value).to_have_text("type")

def test_data_table_visibility(page: Page):
    """Проверяем отображение таблицы с данными"""
    page.goto("http://localhost:8050/")
    
    # Проверяем наличие таблицы
    table = page.locator(".cell-table")
    expect(table).to_be_visible()
    
    # Проверяем наличие хотя бы одной строки данных
    rows = page.locator(".dash-table-container .dash-cell")
    expect(rows.first).to_be_visible()

def test_graph_rendering(page: Page):
    """Проверяем отрисовку графика"""
    page.goto("http://localhost:8050/")
    
    # Проверяем наличие графика
    graph = page.locator("#graph")
    expect(graph).to_be_visible()
    
    # Скриншот графика
    graph.screenshot(path="playwright-tests/screenshots/graph_rendered.png")

def test_data_table_pagination(page: Page):
    """Тестируем пагинацию таблицы"""
    page.goto("http://localhost:8050/")
    
    # Переход на следующую страницу таблицы
    next_page_button = page.locator('.dash-table-container .next-page')
    expect(next_page_button).to_be_visible()
    
    # Перейдем на следующую страницу
    next_page_button.click()
    
    # Проверим, что на странице новые строки
    rows = page.locator(".dash-table-container .dash-cell")
    expect(rows.first).to_be_visible()
