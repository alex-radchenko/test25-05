from selenium import webdriver
from selenium.webdriver.common.by import By

capabilities = {
    "browserName": "chrome",
    "version": "84.0",
    "enableVNC": True,
    "enableVideo": False
}

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities)

login_at = "radwexe@mail.ru"
pass_at = "111"

driver.get("https://auth.1iu.ru")
driver.find_element(By.XPATH, "//input[@name='login']").send_keys('radwexe@mail.ru')
driver.find_element(By.XPATH, "//input[@name='password']").send_keys('111')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
a = driver.find_element(By.XPATH, "//a[contains(text(),'antitreningi.ru')]").get_attribute('href')
print(a)
with open('helper.py', 'w') as f:
    f.write('token = "' + a.split('=')[1] + '"')
driver.close()