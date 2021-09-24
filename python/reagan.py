from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
import pyautogui



driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://www.wikifeetx.com/Reagan_Foxx#&gid=1&pid=5937334")
sleep(3)
for i in range (200):
    required_image = driver.find_element_by_tag_name('body');
    action.context_click(required_image).perform()
    sleep(1)
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.press('right')







sleep(2)

#pyautogui.moveTo(120, 130, duration=1)

        # login_field = self.driver.find_element_by_xpath(
        #     '//*[@id="login_field"]').send_keys(username)
        # password_field = self.driver.find_element_by_xpath(
        #     '//*[@id="password"]').send_keys(pw)
        # login_butt = self.driver.find_element_by_xpath(
        #     '//*[@id="login"]/div[4]/form/div/input[12]').click()
        # self.driver.get("https://github.com/new")
        # sleep(2)
        # repo_field = self.driver.find_element_by_xpath(
        #     '//*[@id="repository_name"]').send_keys(project_name)
        # sleep(2)
        # check_butt = self.driver.find_element_by_xpath(
        #     '//*[@id="repository_auto_init"]').click()
        # sleep(2)
        # create_butt = self.driver.find_element_by_xpath(
        #     '//*[@id="new_repository"]/div[4]/button').click()
        # sleep(4)
#driver.close()
