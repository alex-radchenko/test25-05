from selenium import webdriver
import browsers

capabilities = browsers.chrome_83
ip_selenoid = "http://128.199.103.130:4444/wd/hub"
dr = webdriver.Remote(
        command_executor=ip_selenoid,
        desired_capabilities=capabilities)