from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver_win32/chromedriver.exe')
driver.maximize_window()

user = {
    "User1" : {
        "Firstname" : "Akira",
        "Lastname" : "Suzuki",
        "Age" : 21,
        "Email" : "suzukiakira@mail.com",
        "Salary" : 4500000, 
        "Departemen" : "IT"
    },

    "User2" : {
        "Firstname" : "Daiki",
        "Lastname" : "Tanaka",
        "Age" : 23,
        "Email" : "tanakadaiki@mail.com",
        "Salary" : 3800000,
        "Departemen" : "Ops"
    },

    "User3" : {
        "Firstname" : "Fumio",
        "Lastname" : "Ito",
        "Age" : 21,
        "Email" : "itoFumio@mail.com",
        "Salary" : 6000000,
        "Departemen" :  "Finance"
    }
    
}

driver.get("https://demoqa.com/webtables")

for key in user:
    driver.find_element_by_id('addNewRecordButton').click()
    driver.find_element_by_id('firstName').send_keys(user[key]["Firstname"])
    driver.find_element_by_id('lastName').send_keys(user[key]["Lastname"])
    driver.find_element_by_id('userEmail').send_keys(user[key]["Email"])
    driver.find_element_by_id('age').send_keys(user[key]["Age"])
    driver.find_element_by_id('salary').send_keys(user[key]["Salary"])
    driver.find_element_by_id('department').send_keys(user[key]["Departemen"])
    driver.find_element_by_id('submit').click()
    
