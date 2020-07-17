from selenium import webdriver
import browsers

capabilities = browsers.chrome_83
dr = webdriver.Remote(
        command_executor="http://128.199.103.130:4444/wd/hub",
        desired_capabilities=capabilities)