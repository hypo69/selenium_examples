# Шпаргалка по Selenium и HTML-тегам

В этой шпаргалке собраны основные HTML-теги и примеры использования Selenium для взаимодействия с ними.

## Основы HTML

### Базовые теги

Эти теги формируют структуру HTML-документа:

*   `<html>`: Корневой элемент HTML-документа. Все остальные теги должны быть вложены в него.
*   `<head>`: Содержит метаданные о документе, такие как заголовок, стили, скрипты, кодировку и т.д. Этот раздел не отображается на самой странице.
*   `<title>`: Заголовок страницы, отображаемый в заголовке окна браузера или вкладки. Важен для SEO и удобства пользователей.
*   `<body>`: Содержит основное содержимое страницы, которое отображается в браузере: текст, изображения, ссылки, формы и т.д.

### Структурные теги (HTML5)

Эти теги помогают организовать контент на странице, делая его более семантичным и доступным:

*   `<header>`: Шапка страницы или раздела. Обычно содержит заголовок, логотип, навигацию.
*   `<nav>`: Навигационный блок. Содержит ссылки для перемещения по сайту.
*   `<main>`: Основное содержимое страницы. Содержит уникальный контент данной страницы.
*   `<article>`: Самостоятельный, независимый контент (например, статья в блоге, новость).
*   `<aside>`: Боковая панель или дополнительный контент, связанный с основным контентом страницы.
*   `<footer>`: Подвал страницы или раздела. Обычно содержит информацию об авторских правах, контакты, ссылки на социальные сети.
*   `<section>`: Раздел документа, тематически обособленный.

### Текстовые теги

Эти теги форматируют текст на странице:

*   `<h1>` - `<h6>`: Заголовки разных уровней (от самого большого до самого маленького). Важны для структуры документа и SEO.
*   `<p>`: Параграф (абзац) текста. Используется для разделения текста на логические блоки.
*   `<br>`: Перенос строки.  (Не требует закрывающего тега) Используется для принудительного переноса текста на новую строку.
*   `<hr>`: Горизонтальная линия. (Не требует закрывающего тега) Используется для визуального разделения контента.
*   `<span>`: Встроенный контейнер для текста или других элементов, используемый для стилизации с помощью CSS.
*   `<strong>`: Определяет важный текст (обычно отображается жирным шрифтом). Указывает на смысловую важность текста.
*   `<em>`: Определяет подчеркнутый текст (обычно отображается курсивом). Указывает на эмфазу или выделение текста.
*   `<code>`: Определяет фрагмент компьютерного кода. Отображает код моноширинным шрифтом.
*   `<pre>`: Предварительно форматированный текст. Отображается с сохранением пробелов и переносов строк.

### Теги для ссылок и изображений

Эти теги позволяют связывать страницы и вставлять изображения:

*   `<a>`: Ссылка (гиперссылка). Используется атрибут `href` для указания URL.
*   `<img>`: Изображение. Используется атрибут `src` для указания пути к изображению, атрибут `alt` для альтернативного текста (отображается, если изображение не загрузилось или для людей с ограниченными возможностями), а также атрибуты `width` и `height` для задания размеров.  (Не требует закрывающего тега)

### Теги для списков

Эти теги позволяют создавать упорядоченные и неупорядоченные списки:

*   `<ul>`: Неупорядоченный список (маркированный).
*   `<ol>`: Упорядоченный список (нумерованный).
*   `<li>`: Элемент списка (как для `<ul>`, так и для `<ol>`).
*   `<dl>`: Список определений.
*   `<dt>`: Термин в списке определений.
*   `<dd>`: Описание термина в списке определений.

### Теги для таблиц

Эти теги позволяют структурировать данные в виде таблиц:

*   `<table>`: Таблица.
*   `<tr>`: Строка таблицы.
*   `<th>`: Заголовочная ячейка таблицы.
*   `<td>`: Ячейка данных таблицы.
*   `<caption>`: Заголовок таблицы.

### Теги для форм

Эти теги позволяют создавать интерактивные формы для сбора данных от пользователя:

*   `<form>`: Форма. Содержит все элементы управления формы.
*   `<input>`: Поле ввода (текст, пароль, кнопка и т.д.). Используется атрибут `type` для указания типа поля.
*   `<textarea>`: Многострочное поле ввода текста.
*   `<select>`: Выпадающий список.
*   `<option>`: Элемент выпадающего списка (внутри `<select>`).
*   `<button>`: Кнопка. Может использоваться для отправки формы или выполнения других действий.
*   `<label>`: Метка для элемента формы. Связывает текст с элементом управления.

### Другие важные теги

*   `<div>`: Блочный контейнер для группировки элементов. Используется для создания логических блоков и стилизации с помощью CSS.
*   `<meta>`: Метаданные о документе (например, кодировка, описание, ключевые слова). (Не требует закрывающего тега, но может иметь закрывающий) Важны для SEO и правильной обработки страницы браузером.
*   `<style>`: Встроенные стили CSS. Позволяет задавать стили оформления непосредственно в HTML-документе.
*   `<script>`: Встроенный или подключенный JavaScript.  Позволяет добавлять интерактивность и динамическое поведение на страницу.

### Пример HTML-документа

```html
<!DOCTYPE html>
<html>
<head>
  <title>Пример HTML</title>
  <meta charset="UTF-8">
</head>
<body>

  <header>
    <h1>Добро пожаловать на мой сайт!</h1>
    <nav>
      <a href="#">Главная</a> | <a href="#">Обо мне</a> | <a href="#">Контакты</a>
    </nav>
  </header>

  <main>
    <article>
      <h2>Это заголовок статьи</h2>
      <p>Это параграф текста.  Здесь может быть больше текста и даже <strong>важный текст</strong>!</p>
      <img src="image.jpg" alt="Описание изображения" width="200" height="150">
    </article>

    <aside>
      <h3>Боковая панель</h3>
      <ul>
        <li>Пункт 1</li>
        <li>Пункт 2</li>
        <li>Пункт 3</li>
      </ul>
    </aside>
  </main>

  <footer>>
    <p>© 2023 Мой сайт</p>
  </footer>

</body>
</html>
```

Для более подробного изучения рекомендуется обратиться к документации HTML на сайтах MDN Web Docs ([https://developer.mozilla.org/](https://developer.mozilla.org/)) или W3Schools ([https://www.w3schools.com/](https://www.w3schools.com/)).

## Взаимодействие с HTML-элементами с помощью Selenium

### Настройка Selenium

1.  **Установите Selenium:**

    ```bash
    pip install selenium
    ```
~~2.  **Установите WebDriver:**~~  

~~*   WebDriver - это драйвер браузера, который позволяет Selenium управлять браузером.~~  
~~*   Скачайте WebDriver для вашего браузера (Chrome, Firefox и т.д.) с официального сайта и поместите его в PATH.~~  
~~*   **Chrome:** [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)~~  
~~*   **Firefox:** [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)~~  

### Поиск элементов

Selenium предоставляет различные способы поиска элементов на веб-странице:

*   `By.TAG_NAME`: Поиск по имени тега (например, `div`, `p`, `a`).
*   `By.ID`: Поиск по атрибуту `id`.
*   `By.CLASS_NAME`: Поиск по атрибуту `class`.
*   `By.CSS_SELECTOR`: Поиск с использованием CSS-селекторов (наиболее гибкий и рекомендуемый способ).
*   `By.XPATH`: Поиск с использованием XPath-выражений (может быть полезен для сложных случаев, но обычно менее читаем, чем CSS-селекторы).
*   `By.LINK_TEXT`: Поиск по тексту ссылки.
*   `By.PARTIAL_LINK_TEXT`: Поиск по части текста ссылки.

### Методы поиска

*   `find_element(by, value)`: Находит *первый* элемент, соответствующий заданным критериям. Возвращает объект `WebElement`.
*   `find_elements(by, value)`: Находит *все* элементы, соответствующие заданным критериям. Возвращает список объектов `WebElement`.

### Получение информации об элементе

После того, как элемент найден, можно получить информацию о нем:

*   `element.tag_name`: Возвращает имя тега элемента.
*   `element.text`: Возвращает текстовое содержимое элемента.
*   `element.get_attribute(attribute_name)`: Возвращает значение указанного атрибута элемента.

### Взаимодействие с элементами

*   `element.click()`: Кликает на элемент (например, кнопку, ссылку, чекбокс).
*   `element.send_keys(text)`: Вводит текст в поле ввода.
*   `element.clear()`: Очищает поле ввода.
*   `element.is_selected()`: Проверяет, выбран ли чекбокс или radio button.

### Примеры кода

#### Получить HTML-теги по `tag_name`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Инициализация драйвера (например, Chrome)
driver = webdriver.Chrome()

# 2. Открытие веб-страницы (замените на ваш URL)
driver.get("https://www.example.com")

# 3. Поиск элементов и получение tag_name
try:
    # Пример 1: Получение tag_name для заголовка
    header = driver.find_element(By.TAG_NAME, "h1")
    header_tag = header.tag_name
    print(f"Tag name заголовка: {header_tag}")

    # Пример 2: Получение tag_name для ссылки
    link = driver.find_element(By.TAG_NAME, "a")
    link_tag = link.tag_name
    print(f"Tag name ссылки: {link_tag}")

    # Пример 3: Получение tag_name для поля ввода
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_tag = input_field.tag_name
    print(f"Tag name поля ввода: {input_tag}")

    # Пример 4: Получение всех параграфов на странице
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        paragraph_tag = paragraph.tag_name
        print(f"Tag name параграфа: {paragraph_tag}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера (когда закончите)
    driver.quit()
```

#### Получить HTML-теги по `id`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Инициализация драйвера (например, Chrome)
driver = webdriver.Chrome()

# 2. Открытие веб-страницы (замените на ваш URL)
driver.get("https://example.com")

# 3. Поиск элемента по ID и получение tag_name
try:
    element = driver.find_element(By.ID, "myUniqueElement")
    tag_name = element.tag_name
    print(f"Tag name элемента с id 'myUniqueElement': {tag_name}")

    # Пример: Если элемент с id - это кнопка, то кликнуть по ней:
    if tag_name == "button":
        element.click()
        print("Кнопка была нажата")
    elif tag_name == "input":
        element.send_keys("Текст в поле ввода")
        print("Текст введен в поле ввода")

except Exception as e:
    print(f"Элемент с id 'myUniqueElement' не найден: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Получить HTML-теги по `class_name`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Инициализация драйвера (например, Chrome)
driver = webdriver.Chrome()

# 2. Открытие веб-страницы (замените на ваш URL)
driver.get("https://example.com")

# 3. Поиск элемента по CSS-селектору и получение tag_name
try:
    # Пример 1: Поиск элемента с классом "my-class"
    element = driver.find_element(By.CSS_SELECTOR, ".my-class")
    tag_name = element.tag_name
    print(f"Tag name элемента с классом 'my-class': {tag_name}")

except Exception as e:
    print(f"Элемент не найден: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Получить HTML-теги по `type`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Поиск элементов input по type и получение tag_name
try:
    # Пример 1: Поиск элемента input с type="text"
    text_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    text_input_tag = text_input.tag_name
    print(f"Tag name элемента input с type='text': {text_input_tag}")

    # Пример 2: Поиск всех элементов input с любым атрибутом type
    all_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type]")
    for input_element in all_inputs:
        input_tag = input_element.tag_name
        input_type = input_element.get_attribute("type")
        print(f"Tag name элемента input с type='{input_type}': {input_tag}")

except Exception as e:
    print(f"Элемент не найден: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Получить HTML-теги по `value`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Поиск элементов по атрибуту value и получение tag_name
try:
    # Пример 1: Поиск input с value="Пример текста"
    input_element = driver.find_element(By.CSS_SELECTOR, "input[value='Пример текста']")
    input_tag = input_element.tag_name
    print(f"Tag name элемента input с value='Пример текста': {input_tag}")

    # Пример 2: Поиск всех элементов с атрибутом value и вывод их tag_name и value
    all_elements = driver.find_elements(By.CSS_SELECTOR, "[value]")
    for element in all_elements:
        element_tag = element.tag_name
        element_value = element.get_attribute("value")
        print(f"Tag name: {element_tag}, value: {element_value}")

except Exception as e:
    print(f"Элемент не найден: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Получить HTML-теги по `text`

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Поиск элемента по текстовому содержимому и получение tag_name
try:
    # Пример 1: Поиск элемента, содержащего точный текст "Пример текста"
    element = driver.find_element(By.XPATH, "//*[text()='Пример текста']")
    tag_name = element.tag_name
    print(f"Tag name элемента с текстом 'Пример текста': {tag_name}")

    # Пример 2: Поиск элемента, содержащего текст "Часть текста" (частичное совпадение)
    element_containing = driver.find_element(By.XPATH, "//*[contains(text(), 'Часть текста')]")
    tag_name_containing = element_containing.tag_name
    print(f"Tag name элемента, содержащего текст 'Часть текста': {tag_name_containing}")

    # Пример 3: Поиск всех элементов, содержащих определенный текст, и вывод их tag_name и text
    all_elements = driver.find_elements(By.XPATH, "//*[contains(text(), 'текст')]")
    for element in all_elements:
        element_tag = element.tag_name
        element_text = element.text
        print(f"Tag name: {element_tag}, text: {element_text}")

except Exception as e:
    print(f"Элемент не найден: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Нажать на кнопку

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Нажатие кнопки
try:
    button_element = driver.find_element(By.ID, "myButton")
    button_element.click()
    print("Кнопка 'Нажми меня' была нажата.")

    # Явное ожидание: ждем, пока элемент с id "новыйЭлемент" не станет видимым (или пока не пройдет 10 секунд)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "новыйЭлемент"))
    )
    print("Элемент 'новыйЭлемент' стал видимым!")


except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Заполнить форму

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Заполнение поля ввода
try:
    input_element = driver.find_element(By.ID, "myInput")

    # Явное ожидание: ждем, пока поле ввода не станет кликабельным (или пока не пройдет 10 секунд)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "myInput"))
    )
    input_element.send_keys("Текст для ввода")
    print("Поле ввода заполнено.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Выбор чекбоксов с одинаковым текстом

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Выбор чекбоксов
try:
    # Явное ожидание: ждем, пока хотя бы один чекбокс с текстом "Вариант 1" не станет кликабельным
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and following-sibling::text()=' Вариант 1']"))
    )

    # Теперь, когда мы знаем, что чекбоксы доступны, находим их и кликаем
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and following-sibling::text()=' Вариант 1']")
    for checkbox in checkboxes:
        checkbox.click()
        print(f"Чекбокс с value '{checkbox.get_attribute('value')}' выбран.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Переключение на третий radio button

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Выбор radio button
try:
    # Явное ожидание: ждем, пока третий radio button не станет кликабельным
    radio3_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "radio3"))
    )
    radio3_element.click()
    print("Третий radio button выбран.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Выбор элемента из выпадающего списка

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Выбор элемента из выпадающего списка
try:
    # Явное ожидание: ждем, пока элемент <select> не станет кликабельным
    select_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mySelect"))
    )
    select = Select(select_element)

    # Выбираем элемент по value
    select.select_by_value("option2")
    print("Выбран элемент с value 'option2'.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Прокрутка страницы к элементу

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Прокрутка к элементу
try:
    scroll_to_element = driver.find_element(By.ID, "scrollToMe")

    # Прокручиваем страницу к элементу
    driver.execute_script("arguments[0].scrollIntoView();", scroll_to_element)

    # Явное ожидание: ждем, пока элемент не станет видимым (или пока не пройдет 10 секунд)
    WebDriverWait(driver, 10).until(
        EC.visibility_of(scroll_to_element)
    )
    print("Страница прокручена к элементу 'scrollToMe', и элемент стал видимым.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

#### Загрузка изображения на страницу

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Путь к изображению (замените на свой)
IMAGE_PATH = "path/to/your/image.jpg"

# 1. Инициализация драйвера
driver = webdriver.Chrome()

# 2. Открытие веб-страницы
driver.get("https://example.com")

# 3. Загрузка изображения
try:
    # Проверка наличия файла изображения
    if not os.path.exists(IMAGE_PATH):
        raise FileNotFoundError(f"Файл изображения не найден по пути: {IMAGE_PATH}")

    # Находим элемент input type="file"
    file_input = driver.find_element(By.ID, "fileUpload")

    # Отправляем путь к файлу в поле загрузки
    file_input.send_keys(os.path.abspath(IMAGE_PATH))
    print(f"Изображение '{IMAGE_PATH}' загружено в поле.")

    # Отправка формы (если нужно)
    #submit_button = driver.find_element(By.TAG_NAME, "button")
    #submit_button.click()
    #print("Форма отправлена")

    # Явное ожидание: ждем, пока не появится сообщение об успешной загрузке (или пока не пройдет 10 секунд)
    #WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.ID, "uploadSuccessMessage"))
    #)
    #print("Файл успешно загружен!")

except FileNotFoundError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # 4. Закрытие браузера
    driver.quit()
```

***


Замени заполнители, такие как `"https://example.com"` и `"path/to/your/image.jpg"`, реальными значениями.

Для корректной работы многих примеров на веб странице должны быть соответствующие элементы, примеры необходимых элементов были предоставлены.

В большинстве случаев `time.sleep()` заменен на `WebDriverWait`, где это имеет смысл. Это повышает надежность и стабильность скриптов.

Для более подробного изучения Selenium на 👉 [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/).

Упражнение для практики: попробуйте написать свой сценарий Selenium для взаимодействия с веб-страницей и элементами на ней.

Задание здесь 👉 [https://github.com/hypo69/selenim_examples/blob/master/src/exercises/1/](https://github.com/hypo69/selenim_examples/blob/master/src/exercises/1/README.MD)


## обработка selenium with xpath, css selector, id, name, class name, link text, partial link text находится здесь 👉 [https://github.com/hypo69/selenim_examples/blob/master/src/exercises/1/](https://github.com/hypo69/selenim_examples/blob/master/src/exercises/1/README.MD)

Удачи! 🚀

