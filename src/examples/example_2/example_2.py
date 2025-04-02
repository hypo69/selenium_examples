"""
Модуль для демонстрации взаимодействия с веб-элементами с использованием Selenium.

Этот модуль содержит функции для автоматизации различных действий на веб-странице,
включая заполнение форм, выбор элементов, загрузку файлов и прокрутку страницы.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from typing import Optional
import time


def interact_with_web_elements(driver: WebDriver, html_file_path: str) -> None:
    """
    Выполняет демонстрационные действия с различными веб-элементами на указанной HTML-странице.

    Args:
        driver: Экземпляр веб-драйвера Selenium.
        html_file_path: Путь к HTML-файлу, с которым необходимо взаимодействовать.
    """

    try:
        driver.get(f"file:///{html_file_path}")
        print(f"Открыта страница: file:///{html_file_path}")

        # 1. Взаимодействие с текстовым полем (myInput)
        input_field: WebElement = driver.find_element(By.ID, "myInput")
        print(f"Исходное значение поля myInput: {input_field.get_attribute('value')}")
        input_field.clear()
        input_field.send_keys("Новый текст, введенный Selenium")
        print(f"Новое значение поля myInput: {input_field.get_attribute('value')}")

        # Нажатие на кнопку "Очистить" (clearButton)
        clear_button: WebElement = driver.find_element(By.ID, "clearButton")
        clear_button.click()
        print(f"Значение поля myInput после нажатия 'Очистить': {input_field.get_attribute('value')}")

        # 2. Взаимодействие с полем пароля (passwordInput)
        password_field: WebElement = driver.find_element(By.ID, "passwordInput")
        password_field.send_keys("MySecretPassword")
        print("В поле пароля введен текст (скрытый)")

        # 3. Взаимодействие с полем email (emailInput)
        email_field: WebElement = driver.find_element(By.ID, "emailInput")
        email_field.send_keys("test@example.com")
        print("В поле email введен текст")

        # 4. Взаимодействие с текстовой областью (textareaInput)
        textarea_field: WebElement = driver.find_element(By.ID, "textareaInput")
        textarea_field.clear()
        textarea_field.send_keys("Текст, введенный в текстовую область через Selenium.\nМногострочный текст.")
        print("В текстовую область введен текст")

        # 5. Выбор значения из выпадающего списка (mySelect)
        select_element: WebElement = driver.find_element(By.ID, "mySelect")
        select: Select = Select(select_element)
        select.select_by_value("option2")
        print("В выпадающем списке выбран Option 2")

        # 6. Установка и снятие флажков (checkbox1, checkbox2)
        checkbox1: WebElement = driver.find_element(By.ID, "checkbox1")
        checkbox2: WebElement = driver.find_element(By.ID, "checkbox2")

        if not checkbox1.is_selected():
            checkbox1.click()
            print("Чекбокс 1 установлен")
        else:
            print("Чекбокс 1 уже установлен")

        if checkbox2.is_selected():
            checkbox2.click()
            print("Чекбокс 2 снят")
        else:
            print("Чекбокс 2 уже снят")

        # 7. Выбор радиокнопки (radio2)
        radio2: WebElement = driver.find_element(By.ID, "radio2")
        radio2.click()
        print("Выбрана радиокнопка 2")

        # 8. Нажатие кнопки (myButton) и ожидание появления элемента (newElement)
        button: WebElement = driver.find_element(By.ID, "myButton")
        button.click()
        print("Нажата кнопка 'Нажми меня'")

        wait: WebDriverWait = WebDriverWait(driver, 10)
        new_element: WebElement = wait.until(EC.visibility_of_element_located((By.ID, "newElement")))
        print("Новый элемент появился на странице")

        # 9. Загрузка файла (fileUpload)
        file_upload: WebElement = driver.find_element(By.ID, "fileUpload")
        # file_upload.send_keys("/path/to/your/file.txt")  # Замените на реальный путь к файлу
        print("Попытка загрузить файл (путь указан)")

        # 10. Прокрутка страницы к элементу (scrollToMe) с использованием JavaScript
        scroll_target: WebElement = driver.find_element(By.ID, "scrollToMe")
        driver.execute_script("arguments[0].scrollIntoView();", scroll_target)
        print("Страница прокручена к элементу scrollToMe")
        time.sleep(2)  # Даем время для просмотра

        # 11. Работа с динамически добавленным элементом
        wait = WebDriverWait(driver, 5) #Ждем максимум 5 секунд
        dynamic_element = wait.until(EC.visibility_of_element_located((By.ID, "новыйЭлемент")))
        print(f"Текст динамически добавленного элемента: {dynamic_element.text}")

        # 12.  Получение атрибутов и стилей (примеры)
        print(f"Класс кнопки submit: {driver.find_element(By.ID, 'myButton').get_attribute('class')}")
        print(f"Цвет фона header: {driver.find_element(By.TAG_NAME, 'header').value_of_css_property('background-color')}")


    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise  # Re-raise the exception to be handled by the caller if needed


def main() -> None:
    """
    Основная функция для запуска демонстрации взаимодействия с веб-элементами.
    """
    try:
        # Укажите путь к вашему HTML-файлу
        url: str = "https://davidka.net/examples/selenium/example_2.html" 
        html_file_path: str = "file:///C:\Users\user\Documents\repos\public_repositories\selenium_examples\src\examples\example_2\html\example_2.html" 

        driver: WebDriver = webdriver.Chrome() # или Firefox(), Edge()

        interact_with_web_elements(driver, html_file_path)

    except Exception as e:
        print(f"Главная функция обнаружила ошибку: {e}")

    finally:
        if 'driver' in locals() and driver: #Проверка, что драйвер был создан
            driver.quit()
            print("Драйвер закрыт.")


if __name__ == "__main__":
    main()