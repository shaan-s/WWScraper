from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from math import ceil
from time import sleep

#When this breaks in the future, here are the css selectors used to find elements. Can be swapped in the event of a UI update:

SEL_num = "margin--r--s"
#Text in footer reading XXX results

SEL_print_buttons = '[aria-label="Print"]'
#Print buttons in each row in table

SEL_next_page = '[aria-label="Go to next page"]'
#Next page button in footer

driver = webdriver.Chrome()
driver.get('https://waterlooworks.uwaterloo.ca/myAccount/co-op/full/applications.htm')

input("""The purpose of this script is to download all job descriptions (via pdf) from applied jobs on WaterlooWorks.

Please LOG IN and navigate to MY APPLICATIONS, then press enter. This will download ALL applications as PDFs.

> """)

#first, fetch num applcations ==> num pages

num_applications = driver.find_element(By.CLASS_NAME, SEL_num)

#assumes 25 apps/page
num_pages = ceil(int(num_applications.get_attribute("innerHTML").split(" ")[0])/25)

print(num_pages, "pages")
for x in range(num_pages):
    sleep(0.5)

    buttons = driver.find_elements(By.CSS_SELECTOR, SEL_print_buttons)

    for button in buttons:
        ActionChains(driver).scroll_by_amount(0, 30).perform()
        sleep(0.1)
        ActionChains(driver).move_to_element(button).click(button).perform()

    next_page = driver.find_element(By.CSS_SELECTOR, SEL_next_page)

    ActionChains(driver).move_to_element(next_page).click(next_page).perform()

input()
driver.quit()
