from selenium.webdriver import Chrome  


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 



driver = Chrome()    

driver.get("https://google.com/")  




search=driver.find_element(By.NAME,"q")
search.send_keys("facebook")
search.send_keys(Keys.RETURN) 



login = driver.find_element(By.PARTIAL_LINK_TEXT,"Facebook – prijava ili registracija")
login.click()


input_email=driver.find_element(By.NAME,"email")
input_password=driver.find_element(By.NAME,"pass")
input_email.send_keys('niko.Nikic@hotmail.com')
input_password.send_keys('banjaluka123')

signInButton = driver.find_element(By.NAME, "login")
signInButton.click()

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.element_to_be_clickable((By.NAME, "login")))

errorMessage = driver.find_element(By.CLASS_NAME, "_9ay7")

assert errorMessage.text == "Adresa e-pošte koju ste unijeli nije povezana s korisničkim računom. Pronađite svoj korisnički račun i prijavite se."


