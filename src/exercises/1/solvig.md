
## Модуль Selenium для извлечения данных с веб-страницы

Этот модуль предоставляет набор функций для извлечения различных элементов данных с веб-страницы, используя библиотеку Selenium.  Он предназначен для автоматизированного тестирования веб-приложений и сбора данных (web scraping).

### Зависимости

*   `selenium`
*   `typing`

### Функции

#### `get_main_heading_text(driver: WebDriver) -> Optional[str]`

Извлекает текст заголовка `<h1>` со страницы.

**Аргументы:**

*   `driver: WebDriver`:  Экземпляр веб-драйвера Selenium, представляющий открытую веб-страницу.

**Возвращает:**

*   `Optional[str]`: Текст заголовка `<h1>`, если он найден.  Возвращает `None`, если заголовок не найден или произошла ошибка при его извлечении.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
heading_text = get_main_heading_text(driver)
if heading_text:
    print(f"Заголовок страницы: {heading_text}")
else:
    print("Заголовок не найден.")
driver.quit()
```
### Код примера
```python
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

```
#### `get_nav_links(driver: WebDriver) -> List[Tuple[str, str]]`

Извлекает URL и текст всех ссылок, находящихся внутри элемента `<nav>`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `List[Tuple[str, str]]`: Список кортежей, где каждый кортеж содержит URL (строка) и текст (строка) ссылки. Возвращает пустой список, если элемент `<nav>` не найден или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
nav_links = get_nav_links(driver)
for url, text in nav_links:
    print(f"URL: {url}, Текст: {text}")
driver.quit()
```

#### `get_first_paragraph_text(driver: WebDriver) -> Optional[str]`

Извлекает текст первого параграфа (`<p>`) с идентификатором `firstParagraph`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Текст первого параграфа, если он найден. Возвращает `None`, если параграф не найден или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
paragraph_text = get_first_paragraph_text(driver)
if paragraph_text:
    print(f"Текст параграфа: {paragraph_text}")
else:
    print("Параграф не найден.")
driver.quit()
```

#### `get_first_paragraph_link_url(driver: WebDriver) -> Optional[str]`

Извлекает URL первой ссылки (`<a>`) внутри параграфа с идентификатором `firstParagraph`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: URL первой ссылки внутри параграфа, если она найдена. Возвращает `None`, если ссылка или параграф не найдены или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
link_url = get_first_paragraph_link_url(driver)
if link_url:
    print(f"URL ссылки: {link_url}")
else:
    print("Ссылка не найдена.")
driver.quit()
```

#### `get_name_input_value(driver: WebDriver) -> Optional[str]`

Извлекает значение атрибута `value` поля ввода (`<input>`) с идентификатором `name`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Значение атрибута `value` поля ввода, если оно найдено. Возвращает `None`, если поле не найдено или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
name_value = get_name_input_value(driver)
if name_value:
    print(f"Значение поля 'Имя': {name_value}")
else:
    print("Поле 'Имя' не найдено.")
driver.quit()
```

#### `get_email_input_placeholder(driver: WebDriver) -> Optional[str]`

Извлекает значение атрибута `placeholder` поля ввода (`<input>`) с идентификатором `email`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Значение атрибута `placeholder` поля ввода, если оно найдено. Возвращает `None`, если поле не найдено или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
email_placeholder = get_email_input_placeholder(driver)
if email_placeholder:
    print(f"Placeholder поля 'Email': {email_placeholder}")
else:
    print("Поле 'Email' не найдено.")
driver.quit()
```

#### `get_selected_gender(driver: WebDriver) -> Optional[str]`

Определяет выбранный пол (`male` или `female`) на основе состояния переключателей (radio buttons) с идентификаторами `male` и `female`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Строку `"male"` или `"female"`, в зависимости от того, какой переключатель выбран. Возвращает `None`, если ни один переключатель не выбран или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
selected_gender = get_selected_gender(driver)
if selected_gender:
    print(f"Выбранный пол: {selected_gender}")
else:
    print("Пол не выбран.")
driver.quit()
```

#### `get_selected_country(driver: WebDriver) -> Optional[str]`

Извлекает значение выбранной страны из выпадающего списка (`<select>`) с идентификатором `country`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Значение выбранной страны, если выпадающий список найден и в нем выбран элемент. Возвращает `None`, если выпадающий список не найден или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
selected_country = get_selected_country(driver)
if selected_country:
    print(f"Выбранная страна: {selected_country}")
else:
    print("Страна не выбрана.")
driver.quit()
```

#### `get_comments_textarea_value(driver: WebDriver) -> Optional[str]`

Извлекает текст из текстовой области (`<textarea>`) с идентификатором `comments`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Текст из текстовой области, если она найдена. Возвращает `None`, если текстовая область не найдена или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
comments_value = get_comments_textarea_value(driver)
if comments_value:
    print(f"Текст в textarea: {comments_value}")
else:
    print("Textarea не найдена.")
driver.quit()
```

#### `is_agree_checkbox_checked(driver: WebDriver) -> bool`

Проверяет, установлен ли флажок (`<input type="checkbox">`) с идентификатором `agree`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `bool`: `True`, если флажок установлен, и `False` в противном случае, или если флажок не найден.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
is_checked = is_agree_checkbox_checked(driver)
if is_checked:
    print("Чекбокс установлен.")
else:
    print("Чекбокс не установлен.")
driver.quit()
```

#### `get_submit_button_text(driver: WebDriver) -> Optional[str]`

Извлекает текст кнопки (`<button>`) с идентификатором `submitButton`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Текст кнопки, если она найдена. Возвращает `None`, если кнопка не найдена или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
button_text = get_submit_button_text(driver)
if button_text:
    print(f"Текст кнопки: {button_text}")
else:
    print("Кнопка не найдена.")
driver.quit()
```

#### `get_js_button_text(driver: WebDriver) -> Optional[str]`

Извлекает текст кнопки, у которой есть атрибут `onclick` (обычно используется для вызова JavaScript).

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: Текст кнопки, если она найдена. Возвращает `None`, если кнопка не найдена или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
js_button_text = get_js_button_text(driver)
if js_button_text:
    print(f"Текст JS кнопки: {js_button_text}")
else:
    print("JS кнопка не найдена.")
driver.quit()
```

#### `get_list_items_text(driver: WebDriver) -> List[str]`

Извлекает текст всех элементов списка (`<li>`) внутри неупорядоченного списка (`<ul>`) с идентификатором `listSection`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `List[str]`: Список строк, представляющих текст каждого элемента списка. Возвращает пустой список, если элемент списка не найден или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
list_items = get_list_items_text(driver)
for item in list_items:
    print(f"Элемент списка: {item}")
driver.quit()
```

#### `get_ordered_list_first_item_id(driver: WebDriver) -> Optional[str]`

Извлекает `id` первого элемента (`<li>`) упорядоченного списка (`<ol>`) с идентификатором `firstItem`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `Optional[str]`: `id` первого элемента списка, если он найден. Возвращает `None`, если элемент списка не найден или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
first_item_id = get_ordered_list_first_item_id(driver)
if first_item_id:
    print(f"ID первого элемента списка: {first_item_id}")
else:
    print("Первый элемент списка не найден.")
driver.quit()
```

#### `get_table_data(driver: WebDriver) -> List[List[str]]`

Извлекает данные из таблицы (`<table>`), находящейся внутри элемента с идентификатором `tableSection`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `List[List[str]]`: Список списков строк, где каждый внутренний список представляет строку таблицы, а элементы строки представляют ячейки таблицы. Возвращает пустой список, если таблица не найдена или произошла ошибка.

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
table_data = get_table_data(driver)
for row in table_data:
    print(f"Строка таблицы: {row}")
driver.quit()
```

#### `is_hidden_element_displayed(driver: WebDriver) -> bool`

Проверяет, отображается ли элемент с идентификатором `hiddenElement`.

**Аргументы:**

*   `driver: WebDriver`: Экземпляр веб-драйвера Selenium.

**Возвращает:**

*   `bool`: `True`, если элемент отображается, и `False` в противном случае (включая случай, когда элемент не найден).

**Пример:**

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
is_displayed = is_hidden_element_displayed(driver)
if is_displayed:
    print("Скрытый элемент отображается.")
else:
    print("Скрытый элемент не отображается или не найден.")
driver.quit()
```

### Использование

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import Options

# Configure Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://davidka.net/examples/selenium/example_1.html")

try:
    heading = get_main_heading_text(driver)
    print(f"Heading: {heading}")

    # Вызов других функций и обработка результатов

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
```

**Важно:**

*   Обязательно установите драйвер для используемого вами браузера (например, ChromeDriver для Chrome).  Убедитесь, что версия драйвера совместима с версией вашего браузера.
*   При работе с динамически загружаемым контентом может потребоваться использовать `WebDriverWait` для ожидания появления элементов на странице.
*   Не забудьте закрыть драйвер после завершения работы, вызвав `driver.quit()`, чтобы освободить ресурсы.
*   В production-среде рекомендуется добавить более надежную обработку исключений и журналирование.
*   Вместо прямого указания ID элементов можно использовать другие локаторы, такие как CSS-селекторы или XPath, если структура HTML более сложная.
*   При извлечении больших объемов данных с веб-сайтов соблюдайте этикет web scraping, чтобы не перегружать сервер.
