from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

 #URL тестируемого сайта
BASE_URL = "http://tech-avito-intern.jumpingcrab.com/"

 #Данные для создания объявления
AD_TITLE = "Тестовое объявление"
AD_PRICE = "100"
AD_DESCRIPTION = "Описание"
AD_IMAGE_URL = "https://example.com/image.jpg"

 #Запуск браузера
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(BASE_URL)

try:
    #Нажимаем кнопку "Создать"
    create_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Создать')]")
    create_button.click()
    time.sleep(2)   #это ожидание загрузки формы

  #Заполняем поля
    driver.find_element(By.ID, "title").send_keys(AD_TITLE)  #это название
    driver.find_element(By.ID, "price").send_keys(AD_PRICE)  #это цена
    driver.find_element(By.ID, "description").send_keys(AD_DESCRIPTION)  #это описание
    driver.find_element(By.ID, "image").send_keys(AD_IMAGE_URL)  #это ссылка на изображение

  #Нажимаем "Сохранить"
    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]")
    save_button.click()
    time.sleep(3)  #это ожидание загрузки главной страницы

 #Проверяем, что объявление появилось в списке
    ads = driver.find_elements(By.CLASS_NAME, "ad-title")
    assert any(AD_TITLE in ad.text for ad in ads), "Объявление не найдено в списке!"

   print(Тест пройден: объявление успешно создано!")

finally:
    driver.quit()  #закрываем браузер