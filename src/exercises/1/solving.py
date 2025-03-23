from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_main_heading_text(driver):
    """Получает текст заголовка h1."""
    try:
        element = driver.find_element(By.ID, "mainHeading")
        return element.text
    except:
        return None

def get_nav_links(driver):
    """Получает URL и текст ссылок из блока nav."""
    try:
        links = driver.find_elements(By.CSS_SELECTOR, "nav a")
        return [(link.get_attribute("href"), link.text) for link in links]
    except:
        return []

def get_first_paragraph_text(driver):
    """Получает текст первого параграфа."""
    try:
        element = driver.find_element(By.ID, "firstParagraph")
        return element.text
    except:
        return None

def get_first_paragraph_link_url(driver):
    """Получает URL ссылки внутри первого параграфа."""
    try:
        link = driver.find_element(By.CSS_SELECTOR, "#firstParagraph a")
        return link.get_attribute("href")
    except:
        return None

def get_name_input_value(driver):
    """Получает значение поля ввода имени."""
    try:
        element = driver.find_element(By.ID, "name")
        return element.get_attribute("value")
    except:
        return None

def get_email_input_placeholder(driver):
    """Получает placeholder поля ввода email."""
    try:
        element = driver.find_element(By.ID, "email")
        return element.get_attribute("placeholder")
    except:
        return None

def get_selected_gender(driver):
    """Определяет выбранный пол (male или female)."""
    try:
        male_radio = driver.find_element(By.ID, "male")
        if male_radio.is_selected():
            return "male"
        female_radio = driver.find_element(By.ID, "female")
        if female_radio.is_selected():
            return "female"
        return None
    except:
        return None

def get_selected_country(driver):
    """Получает значение выбранной страны из выпадающего списка."""
    try:
        select_element = driver.find_element(By.ID, "country")
        select = Select(select_element)
        return select.first_selected_option.get_attribute("value")
    except:
        return None

def get_comments_textarea_value(driver):
    """Получает значение поля textarea для комментариев."""
    try:
        element = driver.find_element(By.ID, "comments")
        return element.text
    except:
        return None

def is_agree_checkbox_checked(driver):
    """Проверяет, выбран ли чекбокс "Я согласен с условиями"."""
    try:
        checkbox = driver.find_element(By.ID, "agree")
        return checkbox.is_selected()
    except:
        return False

def get_submit_button_text(driver):
    """Получает текст кнопки отправки."""
    try:
        button = driver.find_element(By.ID, "submitButton")
        return button.text
    except:
        return None

def get_js_button_text(driver):
    """Получает текст кнопки, вызывающей JavaScript alert."""
    try:
        button = driver.find_element(By.CSS_SELECTOR, "button[onclick]")
        return button.text
    except:
        return None

def get_list_items_text(driver):
    """Получает текст всех элементов списка."""
    try:
        items = driver.find_elements(By.CSS_SELECTOR, "#listSection ul li")
        return [item.text for item in items]
    except:
        return []

def get_ordered_list_first_item_id(driver):
     """Получает id первого элемента упорядоченного списка."""
     try:
          item = driver.find_element(By.ID, "firstItem")
          return item.get_attribute("id")
     except:
          return None

def get_table_data(driver):
    """Получает данные из таблицы."""
    try:
        table_data = []
        rows = driver.find_elements(By.CSS_SELECTOR, "#tableSection table tbody tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            table_data.append([cell.text for cell in cells])
        return table_data
    except:
        return []

def is_hidden_element_displayed(driver):
        """Проверяет, отображается ли скрытый элемент. Возвращает False если не отображается, или элемент не найден."""
        try:
            element = driver.find_element(By.ID, "hiddenElement")
            return element.is_displayed()
        except:
            return False #Элемент не отображается или не найден


# --- Основной код ---
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
url = "https://davidka.net/examples/selenium/example_1.html"
driver.get(url)

try:

    # 3. Вызов функций и вывод результатов
    print("Заголовок страницы:", get_main_heading_text(driver))

    nav_links = get_nav_links(driver)
    print("Ссылки в навигации:")
    for url, text in nav_links:
        print(f"\t- URL: {url}, Текст: {text}")

    print("Текст первого параграфа:", get_first_paragraph_text(driver))
    print("URL ссылки в первом параграфе:", get_first_paragraph_link_url(driver))
    print("Значение поля 'Имя':", get_name_input_value(driver))
    print("Placeholder поля 'Email':", get_email_input_placeholder(driver))
    print("Выбранный пол:", get_selected_gender(driver))
    print("Выбранная страна:", get_selected_country(driver))
    print("Текст в textarea 'Комментарии':", get_comments_textarea_value(driver))
    print("Чекбокс 'Согласен' выбран:", is_agree_checkbox_checked(driver))
    print("Текст кнопки 'Отправить':", get_submit_button_text(driver))
    print("Текст кнопки с JavaScript:", get_js_button_text(driver))

    list_items = get_list_items_text(driver)
    print("Элементы списка:")
    for item in list_items:
        print(f"\t- {item}")

    print("id первого элемента упорядоченного списка:", get_ordered_list_first_item_id(driver))

    table_data = get_table_data(driver)
    print("Данные таблицы:")
    for row in table_data:
        print(f"\t{row}")

    print("Скрытый элемент отображается:", is_hidden_element_displayed(driver))

except Exception as e:
     print(f"Общая ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()