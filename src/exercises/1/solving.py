from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from typing import List, Tuple, Optional

def get_main_heading_text(driver: WebDriver) -> Optional[str]:
    """
    Получает текст заголовка h1.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Текст заголовка h1, или None, если заголовок не найден или произошла ошибка.
    """
    try:
        element: WebElement = driver.find_element(By.ID, "mainHeading")
        return element.text
    except Exception:
        return None

def get_nav_links(driver: WebDriver) -> List[Tuple[str, str]]:
    """
    Получает URL и текст ссылок из блока nav.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Список кортежей, содержащих URL и текст каждой ссылки в блоке nav.
        Возвращает пустой список, если блок nav не найден или произошла ошибка.
    """
    try:
        links: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, "nav a")
        return [(link.get_attribute("href"), link.text) for link in links]
    except Exception:
        return []

def get_first_paragraph_text(driver: WebDriver) -> Optional[str]:
    """
    Получает текст первого параграфа.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Текст первого параграфа, или None, если параграф не найден или произошла ошибка.
    """
    try:
        element: WebElement = driver.find_element(By.ID, "firstParagraph")
        return element.text
    except Exception:
        return None

def get_first_paragraph_link_url(driver: WebDriver) -> Optional[str]:
    """
    Получает URL ссылки внутри первого параграфа.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        URL ссылки внутри первого параграфа, или None, если ссылка не найдена или произошла ошибка.
    """
    try:
        link: WebElement = driver.find_element(By.CSS_SELECTOR, "#firstParagraph a")
        return link.get_attribute("href")
    except Exception:
        return None

def get_name_input_value(driver: WebDriver) -> Optional[str]:
    """
    Получает значение поля ввода имени.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Значение поля ввода имени, или None, если поле не найдено или произошла ошибка.
    """
    try:
        element: WebElement = driver.find_element(By.ID, "name")
        return element.get_attribute("value")
    except Exception:
        return None

def get_email_input_placeholder(driver: WebDriver) -> Optional[str]:
    """
    Получает placeholder поля ввода email.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Placeholder поля ввода email, или None, если поле не найдено или произошла ошибка.
    """
    try:
        element: WebElement = driver.find_element(By.ID, "email")
        return element.get_attribute("placeholder")
    except Exception:
        return None

def get_selected_gender(driver: WebDriver) -> Optional[str]:
    """
    Определяет выбранный пол (male или female).

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Строку "male" или "female", в зависимости от выбранного пола, или None,
        если ни один из вариантов не выбран или произошла ошибка.
    """
    try:
        male_radio: WebElement = driver.find_element(By.ID, "male")
        if male_radio.is_selected():
            return "male"
        female_radio: WebElement = driver.find_element(By.ID, "female")
        if female_radio.is_selected():
            return "female"
        return None
    except Exception:
        return None

def get_selected_country(driver: WebDriver) -> Optional[str]:
    """
    Получает значение выбранной страны из выпадающего списка.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Значение выбранной страны, или None, если выпадающий список не найден или произошла ошибка.
    """
    try:
        select_element: WebElement = driver.find_element(By.ID, "country")
        select: Select = Select(select_element)
        return select.first_selected_option.get_attribute("value")
    except Exception:
        return None

def get_comments_textarea_value(driver: WebDriver) -> Optional[str]:
    """
    Получает значение поля textarea для комментариев.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Значение поля textarea для комментариев, или None, если поле не найдено или произошла ошибка.
    """
    try:
        element: WebElement = driver.find_element(By.ID, "comments")
        return element.text
    except Exception:
        return None

def is_agree_checkbox_checked(driver: WebDriver) -> bool:
    """
    Проверяет, выбран ли чекбокс "Я согласен с условиями".

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        True, если чекбокс выбран, и False в противном случае, или если произошла ошибка.
    """
    try:
        checkbox: WebElement = driver.find_element(By.ID, "agree")
        return checkbox.is_selected()
    except Exception:
        return False

def get_submit_button_text(driver: WebDriver) -> Optional[str]:
    """
    Получает текст кнопки отправки.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Текст кнопки отправки, или None, если кнопка не найдена или произошла ошибка.
    """
    try:
        button: WebElement = driver.find_element(By.ID, "submitButton")
        return button.text
    except Exception:
        return None

def get_js_button_text(driver: WebDriver) -> Optional[str]:
    """
    Получает текст кнопки, вызывающей JavaScript alert.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Текст кнопки, вызывающей JavaScript alert, или None, если кнопка не найдена или произошла ошибка.
    """
    try:
        button: WebElement = driver.find_element(By.CSS_SELECTOR, "button[onclick]")
        return button.text
    except Exception:
        return None

def get_list_items_text(driver: WebDriver) -> List[str]:
    """
    Получает текст всех элементов списка.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Список строк, содержащих текст каждого элемента списка.
        Возвращает пустой список, если список не найден или произошла ошибка.
    """
    try:
        items: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, "#listSection ul li")
        return [item.text for item in items]
    except Exception:
        return []

def get_ordered_list_first_item_id(driver: WebDriver) -> Optional[str]:
    """
    Получает id первого элемента упорядоченного списка.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        id первого элемента упорядоченного списка, или None, если элемент не найден или произошла ошибка.
    """
    try:
        item: WebElement = driver.find_element(By.ID, "firstItem")
        return item.get_attribute("id")
    except Exception:
        return None

def get_table_data(driver: WebDriver) -> List[List[str]]:
    """
    Получает данные из таблицы.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        Список списков строк, представляющих данные из таблицы.
        Возвращает пустой список, если таблица не найдена или произошла ошибка.
    """
    try:
        table_data: List[List[str]] = []
        rows: List[WebElement] = driver.find_elements(By.CSS_SELECTOR, "#tableSection table tbody tr")
        for row in rows:
            cells: List[WebElement] = row.find_elements(By.TAG_NAME, "td")
            table_data.append([cell.text for cell in cells])
        return table_data
    except Exception:
        return []

def is_hidden_element_displayed(driver: WebDriver) -> bool:
    """
    Проверяет, отображается ли скрытый элемент. Возвращает False если не отображается, или элемент не найден.

    Args:
        driver: Экземпляр веб-драйвера Selenium.

    Returns:
        True, если скрытый элемент отображается, и False в противном случае, или если элемент не найден.
    """
    try:
        element: WebElement = driver.find_element(By.ID, "hiddenElement")
        return element.is_displayed()
    except Exception:
        return False  # Элемент не отображается или не найден


# --- Основной код ---

# 1. Инициализация драйвера
driver: WebDriver = webdriver.Chrome()

# 2. Открытие веб-страницы
url: str = "https://davidka.net/examples/selenium/example_1.html"
driver.get(url)

try:

    # 3. Вызов функций и вывод результатов
    print("Заголовок страницы:", get_main_heading_text(driver))

    nav_links: List[Tuple[str, str]] = get_nav_links(driver)
    print("Ссылки в навигации:")
    for url_link, text in nav_links:
        print(f"\t- URL: {url_link}, Текст: {text}")

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

    list_items: List[str] = get_list_items_text(driver)
    print("Элементы списка:")
    for item in list_items:
        print(f"\t- {item}")

    print("id первого элемента упорядоченного списка:", get_ordered_list_first_item_id(driver))

    table_data: List[List[str]] = get_table_data(driver)
    print("Данные таблицы:")
    for row in table_data:
        print(f"\t{row}")

    print("Скрытый элемент отображается:", is_hidden_element_displayed(driver))

except Exception as e:
    print(f"Общая ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()