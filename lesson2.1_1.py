from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

n1_text = browser.find_element_by_css_selector("#num1.nowrap")
n1  = n1_text.text
n2_text = browser.find_element_by_css_selector("#num2.nowrap")
n2 = n2_text.text
sum = str(int(n1) + int(n2))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum)

button = browser.find_element_by_xpath("//button[text()='Отправить']")
button.click()