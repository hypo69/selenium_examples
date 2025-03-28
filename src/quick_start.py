from typing import Optional
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Scenario:

    # 2. Открытие HTML-фрагмента
    html_content:str = """
    <div id='article'>
      <div class='article title'>Article</div>
      <div class='summary'><h1>Article for the magazine</h1></div>

      <div font color=red>Title</div>
      <div id = 'chapter'> Chapter 1 </div>
      <div id = 'chapter'> Chapter 2</div>
      <div id = 'chapter'> Chapter 3 </div>
      <button id="myButton">Нажми меня</button>
      <input type="text" id="myInput" value="">

      <div>
        <input type="checkbox" name="option" value="checkbox1"> Вариант 1
        <input type="checkbox" name="option" value="checkbox2"> Вариант 1
        <input type="checkbox" name="option" value="checkbox3"> Вариант 1
      </div>

      <div>
        <input type="radio" id="radio1" name="radioGroup" value="radio1"> Option 1<br>
        <input type="radio" id="radio2" name="radioGroup" value="radio2"> Option 2<br>
        <input type="radio" id="radio3" name="radioGroup" value="radio3"> Option 3<br>
      </div>

      <select id="mySelect">
        <option value="option1">Option 1</option>
        <option value="option2">Option 2</option>
        <option value="option3">Option 3</option>
      </select>

      <div style="height: 2000px;"></div>
      <div id="scrollToMe">Этот элемент внизу страницы</div>
    </div>
    """

    driver : Chrome | Firefox

    def __init__(self, driver_name:Optional[str] = 'firefox'):
        """Определям какой из драйверов запустить"""
        if driver_name == 'chrome':
            self.driver = Chrome()
        elif driver_name == 'firefox':
            self.driver = Firefox()
        else:
            raise ValueError('Invalid driver name')

    def load_local_content(self, html_content:Optional[str] = None):
        """Загружает локальный HTML-фрагмент."""
        return self.driver.get("data:text/html;charset=utf-8," + html_content if html_content else self.html_content)

    def get_article_title(self) -> str | bool:
        """Получает заголовок статьи."""
        try:
            article_title_element = self.driver.find_element(By.CSS_SELECTOR, "#article .article.title")
            return article_title_element.text
        except Exception as ex:
            print(f"Ошибка при получении заголовка статьи: {ex}")
            return False

    def get_magazine_title(self) -> str | bool:
        """Получает заголовок журнала."""
        try:
            magazine_title_element = self.driver.find_element(By.XPATH, "//div[@class='summary']/h1")
            return magazine_title_element.text
        except Exception as ex:
            print(f"Ошибка при получении заголовка журнала: {ex}")
            return False

    def get_chapters(self) -> list[str] | bool:
        """Получает список глав."""
        try:
            chapter_elements = self.driver.find_elements(By.ID, "chapter")
            return [chapter.text for chapter in chapter_elements]
        except Exception as ex:
            print(f"Ошибка при получении глав: {ex}")
            return False

    def click_button(self, button_id: str) -> bool:
        """Нажимает кнопку с указанным ID."""
        try:
            button_element = self.driver.find_element(By.ID, button_id)
            button_element.click()
            print(f"Кнопка с ID '{button_id}' была нажата.")
            return True
        except Exception as ex:
            print(f"Ошибка при нажатии кнопки '{button_id}': {ex}")
            return False

    def fill_input_field(self, input_id: str, text: str) -> bool:
        """Заполняет поле ввода с указанным ID текстом."""
        try:
            input_element = self.driver.find_element(By.ID, input_id)
            input_element.send_keys(text + Keys.TAB)
            print(f"Поле ввода с ID '{input_id}' заполнено текстом '{text}'.")
            return True
        except Exception as ex:
            print(f"Ошибка при заполнении поля ввода '{input_id}': {ex}")
            return False

    def select_checkboxes(self, checkbox_text: str) -> bool:
        """Выбирает чекбоксы с указанным текстом."""
        try:
            checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox' and following-sibling::text()=' " + checkbox_text + "']")
            for checkbox in checkboxes:
                checkbox.click()
                print(f"Чекбокс с value '{checkbox.get_attribute('value')}' выбран.")
            return True
        except Exception as ex:
            print(f"Ошибка при выборе чекбоксов с текстом '{checkbox_text}': {ex}")
            return False

    def select_radio_button(self, radio_id: str) -> bool:
        """Выбирает radio button с указанным ID."""
        try:
            radio_element = self.driver.find_element(By.ID, radio_id)
            radio_element.click()
            print(f"Radio button с ID '{radio_id}' выбран.")
            return True
        except Exception as ex:
            print(f"Ошибка при выборе radio button '{radio_id}': {ex}")
            return False

    def select_dropdown_option(self, select_id: str, option_value: str) -> bool:
        """Выбирает option из выпадающего списка с указанным ID по value."""
        try:
            select_element = self.driver.find_element(By.ID, select_id)
            select = Select(select_element)
            select.select_by_value(option_value)
            print(f"Выбран элемент с value '{option_value}' из выпадающего списка с ID '{select_id}'.")
            return True
        except Exception as ex:
            print(f"Ошибка при выборе элемента выпадающего списка '{select_id}': {ex}")
            return False

    def scroll_to_element(self, element_id: str) -> bool:
        """Прокручивает страницу к элементу с указанным ID."""
        try:
            element = self.driver.find_element(By.ID, element_id)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            print(f"Страница прокручена к элементу с ID '{element_id}'.")
            return True
        except Exception as ex:
            print(f"Ошибка при прокрутке к элементу '{element_id}': {ex}")
            return False

    def quit(self) -> None:
        """Закрывает браузер."""
        self.driver.quit()

def create_report(article_title: str, magazine_title: str, chapters: list[str], filename: str = "article.md") -> bool:
    """Создает Markdown-отчет с указанными данными."""
    markdown_content = f"""# {article_title}

## {magazine_title}

1. {chapters[0]}
2. {chapters[1]}
3. {chapters[2]}
"""

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Markdown-файл {filename} успешно создан.")
        return True
    except Exception as e:
        print(f"Ошибка при создании файла отчета: {e}")
        return False


def run_examples() -> None:
    """Выполняет примеры Selenium и создает отчет."""
    s: Scenario = Scenario(driver_name='firefox')


    try:
        s.load_local_content()

        # 3.1. Получение данных
        article_title = s.get_article_title()
        magazine_title = s.get_magazine_title()
        chapters = s.get_chapters()

        #Проверка на то, что все данные получены успешно
        if not all ([article_title, magazine_title, chapters]):
            print("Не удалось получить все данные для отчета")
            return

        # 3.2. Выполнение действий на странице
        s.click_button("myButton")
        s.fill_input_field("myInput", "Текст для ввода")
        s.select_checkboxes("Вариант 1")
        s.select_radio_button("radio3")
        s.select_dropdown_option("mySelect", "option2")
        s.scroll_to_element("scrollToMe")

        # 3.3. Пауза для визуальной проверки (рекомендуется заменить на WebDriverWait)
        time.sleep(2)

        # 4. Создание отчета
        create_report(article_title, magazine_title, chapters)


    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # 6. Закрытие браузера
        s.quit()


if __name__ == "__main__":
    run_examples()