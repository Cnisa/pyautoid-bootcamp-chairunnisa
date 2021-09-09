from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver.exe')
driver.minimize_window()
url_address = ['noobtest.id', 'erzaf.com', 'orangsiber.com', 'demoqa.com', 'automatetheboringstuff.com']

for x in url_address:
    if url_address == 'orangsiber.com':
        driver.get('https://www.' + x +'/')
        set_title = driver.title
        print(x,' - ', set_title)
    else:
        driver.get('https://' + x +'/')
        set_title = driver.title
        print(x,' - ', set_title)       


driver.close()


