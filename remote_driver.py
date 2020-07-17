ip_selenoid = "http://128.199.103.130:4444/wd/hub"


capabilities = browsers.chrome_84
driver = webdriver.Remote(
    command_executor=remote_driver.ip_selenoid,
    desired_capabilities=capabilities)
driver.maximize_window()