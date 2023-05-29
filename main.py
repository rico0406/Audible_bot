from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd



options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')

web = "https://www.audible.com/search"
driver = webdriver.Chrome(options=options)
driver.get(web)

# pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = pages[-2].text

book_title = []
author = []
run_time = []

for i in range(int(last_page)):
    container = WebDriverWait(driver, 5)\
        .until(EC.presence_of_element_located((By.CLASS_NAME, 'adbl-impression-container')))
    products = WebDriverWait(container, 5) \
        .until(EC.presence_of_all_elements_located((By.XPATH, './/li[contains(@class, "productListItem")]')))

    for product in products:
        print('.')
        book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        run_time.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

    df_books = pd.DataFrame({'title': book_title, 'author': author, 'lenght': run_time})
    df_books.to_csv('books.csv', index=False)
    # products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')