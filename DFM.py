import selenium, time, json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


Name = ""
Pass = ""

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option('useAutomationExtension', False)          
driver = webdriver.Chrome(options=options) 


driver.get("https://www.drfrostmaths.com/login.php?url=https://www.drfrostmaths.com/")
driver.find_element(By.NAME, "login-email").send_keys(Name)
driver.find_element(By.NAME, "login-password").send_keys(Pass)
driver.find_element(By.ID, "login-submit-button").send_keys(Keys.ENTER)


time.sleep(2)
driver.get("https://www.drfrostmaths.com/timestables-game.php")
driver.find_element(By.CLASS_NAME, "very-large-button-variant").send_keys(Keys.ENTER)

time.sleep(1)
driver.execute_script("timeElapsed = 7200")

q = driver.find_element(By.ID, "question").text
if "÷" in q:
    Ans = q.split("÷")
    Ans2 = int(int(Ans[0])/int(Ans[1]))
else:
    Ans = q.split("×")
    Ans2 = int(int(Ans[0])*int(Ans[1]))

driver.find_element(By.ID, "calculator-display").send_keys(Ans2)
while True:
    try:
        driver.execute_script("questionNum = 1")
        driver.find_element(By.ID, "calculator-display").send_keys(Ans2)
    except Exception:
        EXIT = input("There has been an ERROR or the script has been\
 completed\nEnter any key to exit script: ")
        break

driver.quit()






