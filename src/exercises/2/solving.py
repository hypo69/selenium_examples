from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Инициализация драйвера (укажите путь к вашему драйверу, если необходимо)
driver = webdriver.Chrome()

# Открытие страницы
driver.get("file:///C:/path/to/your/html/file.html")  # Замените на реальный путь

try:
    # 1. Взаимодействие с текстовым полем (myInput)
    input_field = driver.find_element(By.ID, "myInput")
    print(f"Исходное значение поля myInput: {input_field.get_attribute('value')}")
    input_field.clear()  # Очистка поля
    input_field.send_keys("Новый текст, введенный Selenium")
    print(f"Новое значение поля myInput: {input_field.get_attribute('value')}")

    # Нажатие на кнопку "Очистить" (clearButton)
    clear_button = driver.find_element(By.ID, "clearButton")
    clear_button.click()
    print(f"Значение поля myInput после нажатия 'Очистить': {input_field.get_attribute('value')}")

    # 2. Взаимодействие с полем пароля (passwordInput)
    password_field = driver.find_element(By.ID, "passwordInput")
    password_field.send_keys("MySecretPassword")
    print("В поле пароля введен текст (скрытый)")

    # 3. Взаимодействие с полем email (emailInput)
    email_field = driver.find_element(By.ID, "emailInput")
    email_field.send_keys("test@example.com")
    print("В поле email введен текст")

    # 4. Взаимодействие с текстовой областью (textareaInput)
    textarea_field = driver.find_element(By.ID, "textareaInput")
    textarea_field.clear()
    textarea_field.send_keys("Текст, введенный в текстовую область через Selenium.\nМногострочный текст.")
    print("В текстовую область введен текст")

    # 5. Выбор значения из выпадающего списка (mySelect)
    select_element = driver.find_element(By.ID, "mySelect")
    select = Select(select_element)
    select.select_by_value("option2")  # Выбор Option 2
    print("В выпадающем списке выбран Option 2")

    # 6. Установка и снятие флажков (checkbox1, checkbox2)
    checkbox1 = driver.find_element(By.ID, "checkbox1")
    checkbox2 = driver.find_element(By.ID, "checkbox2")

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
    radio2 = driver.find_element(By.ID, "radio2")
    radio2.click()
    print("Выбрана радиокнопка 2")

    # 8. Нажатие кнопки (myButton) и ожидание появления элемента (newElement)
    button = driver.find_element(By.ID, "myButton")
    button.click()
    print("Нажата кнопка 'Нажми меня'")

    wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд
    new_element = wait.until(EC.visibility_of_element_located((By.ID, "newElement")))
    print("Новый элемент появился на странице")

    # 9. Загрузка файла (fileUpload)
    file_upload = driver.find_element(By.ID, "fileUpload")
    #file_upload.send_keys("/path/to/your/file.txt") #Замените на реальный путь к файлу.  В целях безопасности браузер может не позволять указывать путь программно
    print("Попытка загрузить файл (путь указан)")

    # 10. Прокрутка страницы к элементу (scrollToMe) с использованием JavaScript
    scroll_target = driver.find_element(By.ID, "scrollToMe")
    driver.execute_script("arguments[0].scrollIntoView();", scroll_target)
    print("Страница прокручена к элементу scrollToMe")
    time.sleep(2) # Даем время для просмотра

    # 11. Работа с динамически добавленным элементом
    wait = WebDriverWait(driver, 5) #Ждем максимум 5 секунд
    dynamic_element = wait.until(EC.visibility_of_element_located((By.ID, "новыйЭлемент")))
    print(f"Текст динамически добавленного элемента: {dynamic_element.text}")

    # 12.  Получение атрибутов и стилей (примеры)
    print(f"Класс кнопки submit: {driver.find_element(By.ID, 'myButton').get_attribute('class')}")
    print(f"Цвет фона header: {driver.find_element(By.TAG_NAME, 'header').value_of_css_property('background-color')}")


except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()