from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from bs4 import BeautifulSoup

print("Предварительная настройка, ждите")

CURRENT_PATH = os.getcwd()
driver_path = f'{CURRENT_PATH}/chromedriver-win64/chromedriver.exe'  # Путь к chromedriver

# Настройки Chrome для отключения загрузки CSS и изображений
chrome_options = Options()
chrome_options.add_argument("--headless")  # Открытие браузера без GUI (можно удалить, если нужен интерфейс)
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Отключаем загрузку изображений и CSS
prefs = {
    "profile.managed_default_content_settings.images": 2,  # Отключить изображения
    "profile.default_content_setting_values.stylesheet": 2,  # Отключить стили
}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Функция для получения HTML-кода страницы
def fetch_page_html(url):
    driver.get(url)
    time.sleep(5)  # Можно использовать WebDriverWait для более надежного ожидания
    return driver.page_source

# Функция для сохранения HTML-кода в файл
def save_html_to_file(html_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

# Функция для получения следующей ссылки
def get_next_link(soup):
    button = soup.find('a', class_='btn is-plain size-lg tz_cb tz_c5 tz_eb')
    if button:
        return 'https://ranobelib.me' + button.get('href').split('?')[0]
    else:
        print('Элемент с указанным классом не найден.')
        return None

# Функция для парсинга HTML и создания нового документа
def create_result_html(tmp_file_name, title_name):
    with open(tmp_file_name, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    h1_tag = soup.find('h1', class_='la_cq')
    div_content = soup.find('div', class_='text-content')

    new_soup = BeautifulSoup('<html><head><title>Result</title></head><body></body></html>', 'html.parser')
    new_soup.body.append(h1_tag)
    new_soup.body.append(div_content)

    with open(title_name, 'a', encoding='utf-8') as file:
        file.write(str(new_soup))
        
print("Предварителььная настройка завершена\n")

# Основная логика
url = str(input("Введите ссылку первой страницы> "))#'https://ranobelib.me/ru/27711--kumo-desu-ga-nani-kaln/read/v14/c1'
next_link = url
tmp_file_name = "tmp_page.html"
title_name = str(input("Введите название результирующего файла> ")) + ".html"#"resulted_page.html"
count_of_pgs = int(input("Введите число страниц, которые хотите скачать> "))


try:
    for _ in range(count_of_pgs):
        
        print(f"\npage {_ + 1}/{count_of_pgs}")
        html_content = fetch_page_html(next_link)
        save_html_to_file(html_content, tmp_file_name)
        with open(tmp_file_name, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
        next_link = get_next_link(soup)
    
        if next_link is None:
            break
        create_result_html(tmp_file_name, title_name)

finally:
    # Закрываем браузер после завершения всех операций
    driver.quit()
print(f"Результат успешно записан в файл {title_name}.")
input("Press any button...")
