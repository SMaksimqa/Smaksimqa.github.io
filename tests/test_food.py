from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_start_page():
  driver = webdriver.Chrome()
  driver.get("https://smaksimqa.github.io/sandwichs.html")
  assert driver.find_element(By.TAG_NAME, "h1").text == "Простой бутерброд с сыром"
  assert driver.find_element(By.TAG_NAME, "h2").text == "Что нужно"
  assert driver.find_element(By.TAG_NAME, "h2").text == "Как приготовить"
  try:
    element = driver.find_element(By.TAG_NAME, "body")
    page_text = element.text
    assert "Намажьте хлеб маслом." in page_text
    assert "Положите сверху ломтик сыра." in page_text
    assert "Добавьте зелень, если хотите." in page_text
    assert "Бутерброд готов!" in page_text
  finally:
    time.sleep(3)
    driver.quit()




