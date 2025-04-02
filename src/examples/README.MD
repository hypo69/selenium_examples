# Шпаргалка по XPATH для Selenium

## HTML
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selenium Training Page</title>
    <style>
        /* Complex CSS for demonstration */
        #container > div.item:nth-child(odd) {
            background-color: #f0f0f0;
        }

        #formSection input[type="text"]:focus + span {
            color: red;
        }

        table#data-table tr:hover {
            background-color: #ffffcc;
        }
    </style>
</head>
<body>

    <h1 id="mainHeading">Selenium Training Example</h1>

    <nav>
        <ul>
            <li><a href="/home" class="nav-link">Home</a></li>
            <li><a href="/about" class="nav-link">About Us</a></li>
            <li id="contact-link"><a href="/contact" class="nav-link">Contact</a></li>
        </ul>
    </nav>

    <div id="content">
        <p id="firstParagraph">
            This is the first paragraph with a <a href="https://example.com" title="Example Link">link to example.com</a>.
        </p>

        <div id="formSection">
            <form action="/submit" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" placeholder="Your Name">
                <span>* Required</span> <br><br>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Your Email">
                <span>* Required</span><br><br>

                <p>Gender:</p>
                <input type="radio" id="male" name="gender" value="male">
                <label for="male">Male</label><br>
                <input type="radio" id="female" name="gender" value="female">
                <label for="female">Female</label><br><br>

                <label for="country">Country:</label>
                <select id="country" name="country">
                    <option value="usa">USA</option>
                    <option value="canada">Canada</option>
                    <option value="uk">UK</option>
                </select><br><br>

                <label for="comments">Comments:</label><br>
                <textarea id="comments" name="comments" rows="4" cols="50"></textarea><br><br>

                <input type="checkbox" id="agree" name="agree">
                <label for="agree">I agree to the terms and conditions</label><br><br>

                <button type="submit" id="submitButton">Submit Form</button>
            </form>
        </div>

        <div id="listSection">
            <h2>List Example</h2>
            <ul>
                <li class="list-item">Item 1</li>
                <li class="list-item">Item 2</li>
                <li class="list-item">Item 3</li>
                <li class="list-item">Item 4</li>
                <li class="list-item">Item 5</li>
            </ul>

            <ol>
                <li id="firstItem">First Item in Ordered List</li>
                <li>Second Item</li>
                <li>Third Item</li>
            </ol>
        </div>

        <div id="tableSection">
            <h2>Table Example</h2>
            <table id="data-table">
                <thead>
                    <tr>
                        <th>Header 1</th>
                        <th>Header 2</th>
                        <th>Header 3</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Row 1, Cell 1</td>
                        <td>Row 1, Cell 2</td>
                        <td>Row 1, Cell 3</td>
                    </tr>
                    <tr>
                        <td>Row 2, Cell 1</td>
                        <td>Row 2, Cell 2</td>
                        <td>Row 2, Cell 3</td>
                    </tr>
                    <tr>
                        <td>Row 3, Cell 1</td>
                        <td>Row 3, Cell 2</td>
                        <td>Row 3, Cell 3</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div id="hiddenSection" style="display: none;">
            <p id="hiddenElement">This element is hidden.</p>
        </div>

        <div id="container">
            <div class="item">Item A</div>
            <div class="item">Item B</div>
            <div class="item">Item C</div>
        </div>

        <button onclick="alert('Hello from JavaScript!');">Click Me!</button>
    </div>

    <footer>
        <p>&copy; 2024 Selenium Training</p>
    </footer>

</body>
</html>
```
## Разбор кода:
Разберем, что делает этот HTML-код, который будет хорошим полигоном для Selenium, 
особенно с акцентом на XPath:

**Разнообразие элементов:**

*   Заголовки (`<h1>`)
*   Навигация (`<nav>`, `<ul>`, `<li>`, `<a>`)
*   Параграфы (`<p>`) с ссылками (`<a>`)
*   Форма (`<form>`, `<label>`, `<input>` (text, email, radio, checkbox), `<select>`, `<textarea>`, `<button>`)
*   Списки (`<ul>`, `<ol>`, `<li>`)
*   Таблицы (`<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`)
*   Скрытые элементы (`<div style="display: none;">`, `<p>`)
*   Элементы `div` с классами.
*   Кнопка с JavaScript (`<button onclick="...">`)
*   `<footer>`

**Сложные CSS (для тренировки CSS-селекторов, но XPath может обойти их):**

*   `:nth-child`
*   `input:focus + span`
*   `:hover`

**Задачи для Selenium (с акцентом на XPath):**

1.  **Заголовок:**
    *   XPath: `//h1[@id='mainHeading']` (Поиск по ID)
    *   XPath: `//h1[text()='Selenium Training Example']` (Поиск по тексту)

2.  **Навигационные ссылки:**
    *   XPath: `//nav//a[@href='/about']` (Поиск вложенных элементов с атрибутом)
    *   XPath: `//nav//li[@id='contact-link']/a` (Поиск дочернего элемента по ID родителя)
    *   XPath: `//a[contains(@class, 'nav-link')]` (Содержит класс)

3.  **Ссылка в параграфе:**
    *   XPath: `//p[@id='firstParagraph']/a[@href='https://example.com']` (Поиск по ID родителя и атрибуту)

4.  **Форма:**
    *   XPath: `//input[@id='name' and @type='text']` (Несколько атрибутов)
    *   XPath: `//label[@for='email']/following-sibling::input[@id='email']` (Поиск следующего элемента за label)
    *   XPath: `//input[@id='male']/following-sibling::label[text()='Male']` (Соседний элемент с текстом)
    *   XPath: `//select[@id='country']/option[@value='uk']` (Поиск элемента option в select)
    *   XPath: `//textarea[@id='comments']`
    *   XPath: `//button[@id='submitButton' and text()='Submit Form']` (Кнопка с текстом)

5.  **Списки:**
    *   XPath: `//ul/li[@class='list-item'][position()=3]` (Поиск по позиции элемента в списке)
    *   XPath: `//ol/li[@id='firstItem']`
    *   XPath: `//li[contains(text(), 'Item')]` (Содержит текст)

6.  **Таблица:**
    *   XPath: `//table[@id='data-table']/tbody/tr[2]/td[3]` (Конкретная ячейка таблицы)
    *   XPath: `//table[@id='data-table']//th[text()='Header 2']` (Поиск заголовка столбца)
    *   XPath: `//table[@id='data-table']//td[contains(text(), 'Row 2')]` (Содержит текст 'Row 2')

7.  **Скрытый элемент:**
    *   XPath: `//div[@id='hiddenSection']/p[@id='hiddenElement']` (Поиск скрытого элемента)

8.  **Элементы DIV с классами и контейнер:**
    *   XPath: `//div[@id='container']/div[@class='item'][1]`  (первый элемент item внутри container)
    *   XPath: `//div[@class='item'][last()]` (последний элемент item)
    *   XPath: `//div[@class='item'][position() mod 2 = 1]` (каждый нечетный item)

9.  **JavaScript Кнопка:**
    *   XPath: `//button[contains(@onclick, 'alert')]` (Кнопка, у которой атрибут onclick содержит текст "alert")

**Примеры XPath с использованием соседей (following-sibling, preceding-sibling, ancestor, descendant):**

*   `//label[@for='name']/following-sibling::input` (Найти input, идущий после label[for='name'])
*   `//input[@id='email']/preceding-sibling::label` (Найти label, идущий перед input[@id='email'])
*   `//table[@id='data-table']/ancestor::div[@id='tableSection']` (Найти div с id="tableSection", который является родителем таблицы)
*   `//div[@id='content']/descendant::a` (Найти все ссылки в div с id="content")

**Как использовать XPath максимально:**

*   **Использовать относительные пути ( `.//`  вместо  `//`):**  Начните поиск от текущего найденного элемента, а не от корня документа.  Это делает XPath более устойчивым к изменениям в структуре документа.
*   **Использовать функции XPath:**
    *   `contains(string, substring)`:  Проверить, содержит ли строка подстроку.
    *   `text()`: Получить текстовое значение элемента.
    *   `@attribute`:  Получить значение атрибута элемента.
    *   `starts-with(string, substring)`:  Проверить, начинается ли строка с подстроки.
    *   `ends-with(string, substring)`: Проверить, заканчивается ли строка подстрокой (нестандартная функция, может не поддерживаться всеми XPath-движками).
    *   `string-length(string)`: Получить длину строки.
    *   `translate(string, from, to)`: Заменить символы в строке.
    *   `normalize-space(string)`:  Удалить лишние пробелы из строки.
*   **Использовать оси (axes) XPath:**
    *   `ancestor`: Найти всех предков элемента.
    *   `descendant`: Найти всех потомков элемента.
    *   `following`: Найти все элементы, идущие после текущего элемента в порядке документа.
    *   `preceding`: Найти все элементы, идущие перед текущим элементом в порядке документа.
    *   `following-sibling`: Найти все следующие элементы одного уровня.
    *   `preceding-sibling`: Найти все предыдущие элементы одного уровня.
    *   `parent`: Найти родительский элемент.
    *   `child`: Найти дочерние элементы.
*   **Использовать условия (предикаты)  `[]`:**  Фильтровать элементы по атрибутам, тексту, позиции и другим условиям.
*   **Комбинировать XPath:** Можно комбинировать несколько XPath, разделяя их символом `|`. Это позволит найти несколько элементов, соответствующих разным критериям, одним запросом.  Например: `//h1 | //h2`.

---

Примеры:
- Получение информации о элементах 👉 [https://github.com/hypo69/selenium_examples/blob/master/src/examples/example_1/example_1.ipynb](https://github.com/hypo69/selenium_examples/blob/master/src/examples/example_1/example_1.ipynb)
- Интерактивное взаимодействие 👉 [https://github.com/hypo69/selenium_examples/blob/master/src/examples/example_2/example_2.ipynb](https://github.com/hypo69/selenium_examples/blob/master/src/examples/example_2/example_2.ipynb)


Удачи! 🚀